using Microsoft.AspNetCore.Mvc;
using ElearningAPI.DTOs;
using ElearningAPI.Services;

namespace ElearningAPI.Controllers
{
    [Route("api/users")]
    [ApiController]
    public class UsersController : ControllerBase
    {
        private readonly IUserService _userService;

        public UsersController(IUserService userService)
        {
            _userService = userService;
        }

        // REGISTER
        [HttpPost("register")]
        public async Task<IActionResult> Register(UserRegisterDTO dto)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            var result = await _userService.Register(dto);

            if (!result.Success)
                return BadRequest(result.Message);

            return Created("", result.Data);
        }

        // LOGIN
        [HttpPost("login")]
        public async Task<IActionResult> Login(LoginDto dto)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            var result = await _userService.Login(dto);

            if (!result.Success)
                return BadRequest(result.Message);

            return Ok(result.Data);
        }

        // GET USER
        [HttpGet("{id}")]
        public async Task<IActionResult> GetUser(int id)
        {
            var result = await _userService.GetUser(id);

            if (!result.Success)
                return NotFound(result.Message);

            return Ok(result.Data);
        }

        // UPDATE USER
        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateUser(int id, UserUpdateDTO dto)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            var result = await _userService.UpdateUser(id, dto);

            if (!result.Success)
                return NotFound(result.Message);

            return Ok(result.Data);
        }
    }
}