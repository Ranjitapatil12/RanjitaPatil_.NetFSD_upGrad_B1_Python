using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ElearningAPI.Data;
using ElearningAPI.DTOs;

namespace ElearningAPI.Controllers
{
    [Route("api/results")] 
    [ApiController]
    public class ResultsController : ControllerBase
    {
        private readonly AppDbContext _context;

        public ResultsController(AppDbContext context)
        {
            _context = context;
        }

        // GET: api/results/{userId}
        [HttpGet("{userId}")]
        public async Task<IActionResult> GetResults(int userId)
        {
            var results = await _context.Results
                .Where(r => r.UserId == userId)
                .AsNoTracking()
                .Select(r => new ResultDTO
                {
                    ResultId = r.ResultId,
                    QuizId = r.QuizId,
                    Score = r.Score,
                    AttemptDate = r.AttemptDate
                })
                .ToListAsync();

            if (!results.Any())
                return NotFound();

            return Ok(results);
        }
    }
}