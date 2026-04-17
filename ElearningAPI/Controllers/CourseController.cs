using Microsoft.AspNetCore.Mvc;
using ElearningAPI.Data;
using ElearningAPI.Models;
using ElearningAPI.DTOs;
using Microsoft.EntityFrameworkCore;
using AutoMapper;

namespace ElearningAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CoursesController : ControllerBase
    {
        private readonly AppDbContext _context;
        private readonly IMapper _mapper;

        public CoursesController(AppDbContext context, IMapper mapper)
        {
            _context = context;
            _mapper = mapper;
        }

        //  GET: api/courses
        [HttpGet]
        public async Task<IActionResult> GetCourses()
        {
            var courses = await _context.Courses
                .AsNoTracking()
                .ToListAsync();

            var result = _mapper.Map<List<CourseDTO>>(courses);

            return Ok(result);
        }

        // GET: api/courses/{id}
        [HttpGet("{id}")]
        public async Task<IActionResult> GetCourse(int id)
        {
            var course = await _context.Courses
                .AsNoTracking()
                .FirstOrDefaultAsync(c => c.CourseId == id);

            if (course == null)
                return NotFound();

            var result = _mapper.Map<CourseDTO>(course);

            return Ok(result);
        }

        // POST: api/courses
        [HttpPost]
        public async Task<IActionResult> CreateCourse(CourseDTO dto)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            var userExists = await _context.Users
                .AnyAsync(u => u.UserId == dto.UserId);

            if (!userExists)
                return BadRequest("Invalid UserId");

            var course = _mapper.Map<Course>(dto);
            course.CreatedAt = DateTime.Now;

            _context.Courses.Add(course);
            await _context.SaveChangesAsync();

            var resultDto = _mapper.Map<CourseDTO>(course);

            return CreatedAtAction(nameof(GetCourse), new { id = course.CourseId }, resultDto);
        }

        //  PUT: api/courses/{id}
        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateCourse(int id, CourseDTO dto)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            var course = await _context.Courses.FindAsync(id);

            if (course == null)
                return NotFound();

            //  FIXED: Manual update (no AutoMapper here)
            course.Title = dto.Title;
            course.Description = dto.Description;

            await _context.SaveChangesAsync();

            return NoContent();
        }

        // DELETE: api/courses/{id}
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteCourse(int id)
        {
            var course = await _context.Courses.FindAsync(id);

            if (course == null)
                return NotFound();

            _context.Courses.Remove(course);
            await _context.SaveChangesAsync();

            return NoContent();
        }
    }
}