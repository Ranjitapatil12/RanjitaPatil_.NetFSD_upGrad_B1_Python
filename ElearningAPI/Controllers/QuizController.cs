using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ElearningAPI.Data;
using ElearningAPI.Models;
using ElearningAPI.DTOs;

namespace ElearningAPI.Controllers
{
    [Route("api/quizzes")]
    [ApiController]
    public class QuizController : ControllerBase
    {
        private readonly AppDbContext _context;

        public QuizController(AppDbContext context)
        {
            _context = context;
        }

        // POST: api/quizzes
        [HttpPost]
        public async Task<IActionResult> CreateQuiz([FromBody] QuizCreateDTO dto)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            var course = await _context.Courses.FindAsync(dto.CourseId);
            if (course == null)
                return BadRequest("Invalid CourseId");

            var quiz = new Quiz
            {
                Title = dto.Title,
                CourseId = dto.CourseId
            };

            _context.Quizzes.Add(quiz);
            await _context.SaveChangesAsync();

            return CreatedAtAction(nameof(GetQuizzesByCourse),
                new { courseId = quiz.CourseId },
                new
                {
                    quiz.QuizId,
                    quiz.Title,
                    quiz.CourseId
                });
        }

        // GET: api/quizzes/{courseId}
        [HttpGet("{courseId}")]
        public async Task<IActionResult> GetQuizzesByCourse(int courseId)
        {
            var quizzes = await _context.Quizzes
                .Where(q => q.CourseId == courseId)
                .AsNoTracking()
                .Select(q => new
                {
                    q.QuizId,
                    q.Title,
                    q.CourseId
                })
                .ToListAsync();

            if (!quizzes.Any())
                return NotFound("No quizzes found for this course");

            return Ok(quizzes);
        }

        //  GET: api/quizzes/{quizId}/questions
        [HttpGet("{quizId}/questions")]
        public async Task<IActionResult> GetQuestionsByQuiz(int quizId)
        {
            var questions = await _context.Questions
                .Where(q => q.QuizId == quizId)
                .AsNoTracking()
                .Select(q => new
                {
                    q.QuestionId,
                    q.QuestionText,
                    q.OptionA,
                    q.OptionB,
                    q.OptionC,
                    q.OptionD
                })
                .ToListAsync();

            if (!questions.Any())
                return NotFound("No questions found for this quiz");

            return Ok(questions);
        }

        //  POST: api/quizzes/{quizId}/submit
        [HttpPost("{quizId}/submit")]
        public async Task<IActionResult> SubmitQuiz(int quizId, [FromBody] QuizSubmitDTO dto)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            //  Validate quiz
            var quiz = await _context.Quizzes
                .Include(q => q.Questions)
                .FirstOrDefaultAsync(q => q.QuizId == quizId);

            if (quiz == null)
                return NotFound("Quiz not found");

            //  Validate user
            var userExists = await _context.Users
                .AnyAsync(u => u.UserId == dto.UserId);

            if (!userExists)
                return BadRequest("Invalid UserId");

            int score = 0;

            foreach (var question in quiz.Questions)
            {
                if (dto.Answers.ContainsKey(question.QuestionId))
                {
                    if (dto.Answers[question.QuestionId] == question.CorrectAnswer)
                        score++;
                }
            }

            var result = new Result
            {
                UserId = dto.UserId,
                QuizId = quizId,
                Score = score,
                AttemptDate = DateTime.UtcNow 
            };

            _context.Results.Add(result);
            await _context.SaveChangesAsync();

            return Ok(new QuizResultDTO
            {
                Score = score,
                Total = quiz.Questions.Count
            });
        }
    }
}