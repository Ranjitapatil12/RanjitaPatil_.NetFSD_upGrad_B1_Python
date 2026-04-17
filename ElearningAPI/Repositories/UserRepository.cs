using ElearningAPI.Data;
using ElearningAPI.Models;
using Microsoft.EntityFrameworkCore;

namespace ElearningAPI.Repositories
{
    public class UserRepository : IUserRepository
    {
        private readonly AppDbContext _context;

        // ✅ Constructor
        public UserRepository(AppDbContext context)
        {
            _context = context;
        }

        // ✅ Get by Email
        public async Task<User?> GetByEmail(string email)
        {
            return await _context.Users
                .FirstOrDefaultAsync(u => u.Email == email);
        }

        // ✅ Get by Id
        public async Task<User?> GetById(int id)
        {
            return await _context.Users
                .FirstOrDefaultAsync(u => u.UserId == id);
        }

        // ✅ Add User
        public async Task AddUser(User user)
        {
            await _context.Users.AddAsync(user);
        }

        // ✅ UPDATE USER (🔥 IMPORTANT ADD)
        public async Task UpdateUser(User user)
        {
            _context.Users.Update(user);
            await Task.CompletedTask; // EF tracks changes
        }

        // ✅ Save Changes
        public async Task Save()
        {
            await _context.SaveChangesAsync();
        }
    }
}