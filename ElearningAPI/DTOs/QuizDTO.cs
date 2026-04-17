using System.ComponentModel.DataAnnotations;

namespace ElearningAPI.DTOs
{
    public class QuizDTO
    {
        public int QuizId { get; set; }

        [Required]
        public string Title { get; set; } = string.Empty;

        [Required]
        public int CourseId { get; set; }
    }
}