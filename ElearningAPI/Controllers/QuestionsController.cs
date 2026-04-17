using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ElearningAPI.Data;
using ElearningAPI.Models;
using ElearningAPI.DTOs;

namespace ElearningAPI.Controllers
{
    [Route("api/questions")] 
    [ApiController]
    public class QuestionsController : ControllerBase
    {
        private readonly AppDbContext _context;

        public QuestionsController(AppDbContext context)
        {
            _context = context;
        }

        // POST: api/questions
        [HttpPost]
        public async Task<IActionResult> AddQuestion(QuestionCreateDTO dto)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            var quiz = await _context.Quizzes.FindAsync(dto.QuizId);

            if (quiz == null)
                return BadRequest("Invalid QuizId");

            var question = new Question
            {
                QuizId = dto.QuizId,
                QuestionText = dto.QuestionText,
                OptionA = dto.OptionA,
                OptionB = dto.OptionB,
                OptionC = dto.OptionC,
                OptionD = dto.OptionD,
                CorrectAnswer = dto.CorrectAnswer
            };

            _context.Questions.Add(question);
            await _context.SaveChangesAsync();

            // RETURN DTO
            var response = new QuestionDTO
            {
                QuestionId = question.QuestionId,
                QuestionText = question.QuestionText,
                OptionA = question.OptionA,
                OptionB = question.OptionB,
                OptionC = question.OptionC,
                OptionD = question.OptionD
            };

            return Ok(response);
        }
    }
}