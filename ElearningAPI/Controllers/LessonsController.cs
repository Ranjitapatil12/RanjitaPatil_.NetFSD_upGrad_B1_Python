using Microsoft.AspNetCore.Mvc;
using ElearningAPI.Data;
using ElearningAPI.Models;
using ElearningAPI.DTOs;
using Microsoft.EntityFrameworkCore;

namespace ElearningAPI.Controllers
{
    [Route("api")]
    [ApiController]
    public class LessonsController : ControllerBase
    {
        private readonly AppDbContext _context;

        public LessonsController(AppDbContext context)
        {
            _context = context;
        }

        // GET: api/courses/{courseId}/lessons
        [HttpGet("courses/{courseId}/lessons")]
        public async Task<IActionResult> GetLessonsByCourse(int courseId)
        {
            var lessons = await _context.Lessons
                .Where(l => l.CourseId == courseId)
                .AsNoTracking()
                .Select(l => new LessonDTO
                {
                    LessonId = l.LessonId,
                    CourseId = l.CourseId,
                    Title = l.Title,
                    Content = l.Content,
                    OrderIndex = l.OrderIndex
                })
                .ToListAsync();

            if (!lessons.Any())
                return NotFound("No lessons found for this course");

            return Ok(lessons);
        }

        // POST: api/lessons
        [HttpPost("lessons")]
        public async Task<IActionResult> CreateLesson(LessonDTO dto)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            var courseExists = await _context.Courses
                .AnyAsync(c => c.CourseId == dto.CourseId);

            if (!courseExists)
                return BadRequest("Invalid CourseId");

            var lesson = new Lesson
            {
                CourseId = dto.CourseId,
                Title = dto.Title,
                Content = dto.Content,
                OrderIndex = dto.OrderIndex
            };

            _context.Lessons.Add(lesson);
            await _context.SaveChangesAsync();

            var resultDto = new LessonDTO
            {
                LessonId = lesson.LessonId,
                CourseId = lesson.CourseId,
                Title = lesson.Title,
                Content = lesson.Content,
                OrderIndex = lesson.OrderIndex
            };

            return CreatedAtAction(nameof(GetLessonsByCourse),
                new { courseId = lesson.CourseId }, resultDto);
        }

        // PUT: api/lessons/{id}
        [HttpPut("lessons/{id}")]
        public async Task<IActionResult> UpdateLesson(int id, LessonDTO dto)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            var lesson = await _context.Lessons.FindAsync(id);

            if (lesson == null)
                return NotFound();

            lesson.Title = dto.Title;
            lesson.Content = dto.Content;
            lesson.OrderIndex = dto.OrderIndex;

            await _context.SaveChangesAsync();

            return NoContent();
        }

        //  DELETE: api/lessons/{id}
        [HttpDelete("lessons/{id}")]
        public async Task<IActionResult> DeleteLesson(int id)
        {
            var lesson = await _context.Lessons.FindAsync(id);

            if (lesson == null)
                return NotFound();

            _context.Lessons.Remove(lesson);
            await _context.SaveChangesAsync();

            return NoContent();
        }
    }
}