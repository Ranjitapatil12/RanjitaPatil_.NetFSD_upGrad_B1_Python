using ElearningAPI.DTOs;
using ElearningAPI.Models;
using ElearningAPI.Repositories;
using BCrypt.Net;

namespace ElearningAPI.Services
{
    public class UserService : IUserService
    {
        private readonly IUserRepository _userRepository;

        public UserService(IUserRepository userRepository)
        {
            _userRepository = userRepository;
        }

        // REGISTER
        public async Task<ApiResponse<object>> Register(UserRegisterDTO dto)
        {
            var existingUser = await _userRepository.GetByEmail(dto.Email);

            if (existingUser != null)
            {
                return new ApiResponse<object>
                {
                    Success = false,
                    Message = "User already exists"
                };
            }

            var user = new User
            {
                FullName = dto.FullName,
                Email = dto.Email,
                PasswordHash = BCrypt.Net.BCrypt.HashPassword(dto.Password),
                CreatedAt = DateTime.Now
            };

            await _userRepository.AddUser(user);
            await _userRepository.Save();

            return new ApiResponse<object>
            {
                Success = true,
                Message = "User registered successfully",
                Data = new
                {
                    user.UserId,
                    user.FullName,
                    user.Email
                }
            };
        }

        // LOGIN
        public async Task<ApiResponse<object>> Login(LoginDto dto)
        {
            var user = await _userRepository.GetByEmail(dto.Email);

            if (user == null)
            {
                return new ApiResponse<object>
                {
                    Success = false,
                    Message = "Invalid email"
                };
            }

            bool isValid = BCrypt.Net.BCrypt.Verify(dto.Password, user.PasswordHash);

            if (!isValid)
            {
                return new ApiResponse<object>
                {
                    Success = false,
                    Message = "Invalid password"
                };
            }

            return new ApiResponse<object>
            {
                Success = true,
                Message = "Login successful",
                Data = new
                {
                    user.UserId,
                    user.FullName,
                    user.Email
                }
            };
        }

        // GET USER
        public async Task<ApiResponse<object>> GetUser(int id)
        {
            var user = await _userRepository.GetById(id);

            if (user == null)
            {
                return new ApiResponse<object>
                {
                    Success = false,
                    Message = "User not found"
                };
            }

            return new ApiResponse<object>
            {
                Success = true,
                Data = new
                {
                    user.UserId,
                    user.FullName,
                    user.Email
                }
            };
        }

        // UPDATE USER
        public async Task<ApiResponse<object>> UpdateUser(int id, UserUpdateDTO dto)
        {
            var user = await _userRepository.GetById(id);

            if (user == null)
            {
                return new ApiResponse<object>
                {
                    Success = false,
                    Message = "User not found"
                };
            }

            user.FullName = dto.FullName;
            user.Email = dto.Email;

            await _userRepository.UpdateUser(user);
            await _userRepository.Save();

            return new ApiResponse<object>
            {
                Success = true,
                Message = "User updated successfully",
                Data = new
                {
                    user.UserId,
                    user.FullName,
                    user.Email
                }
            };
        }
    }
}