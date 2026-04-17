using System.ComponentModel.DataAnnotations;

namespace ElearningAPI.DTOs
{
    public class QuizCreateDTO
    {
        [Required]
        [MinLength(3)]
        public string Title { get; set; } = string.Empty;

        [Required]
        public int CourseId { get; set; }
    }
}