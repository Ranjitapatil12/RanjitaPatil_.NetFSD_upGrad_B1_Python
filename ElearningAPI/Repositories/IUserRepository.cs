using ElearningAPI.Models;

namespace ElearningAPI.Repositories
{
    public interface IUserRepository
    {
        Task<User?> GetByEmail(string email);
        Task<User?> GetById(int id);
        Task AddUser(User user);
        Task UpdateUser(User user); 
        Task Save();
    }
}