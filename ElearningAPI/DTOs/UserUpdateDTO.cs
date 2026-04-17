using System.ComponentModel.DataAnnotations;

namespace ElearningAPI.DTOs
{
    public class UserUpdateDTO
    {
        [Required]
        public string FullName { get; set; } = string.Empty;

        [Required]
        [EmailAddress]
        public string Email { get; set; } = string.Empty;
    }
}