using System.ComponentModel.DataAnnotations;

namespace ElearningAPI.DTOs
{
    public class CourseDTO
    {
        public int CourseId { get; set; }

        [Required]
        public string Title { get; set; } = string.Empty;

        [Required]
        public string Description { get; set; } = string.Empty;

        [Required]
        public int UserId { get; set; }
    }
}