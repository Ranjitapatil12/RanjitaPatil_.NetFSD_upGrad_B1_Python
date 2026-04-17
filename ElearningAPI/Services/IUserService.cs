using ElearningAPI.DTOs;

namespace ElearningAPI.Services
{
    public interface IUserService
    {
        Task<ApiResponse<object>> Register(UserRegisterDTO dto);
        Task<ApiResponse<object>> Login(LoginDto dto);
        Task<ApiResponse<object>> GetUser(int id);
        Task<ApiResponse<object>> UpdateUser(int id, UserUpdateDTO dto);
    }
}