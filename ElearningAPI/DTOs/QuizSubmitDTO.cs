using System.ComponentModel.DataAnnotations;

namespace ElearningAPI.DTOs
{
    public class QuizSubmitDTO
    {
        [Required]
        public int UserId { get; set; }

        [Required]
        public Dictionary<int, string> Answers { get; set; } = new();
    }
}