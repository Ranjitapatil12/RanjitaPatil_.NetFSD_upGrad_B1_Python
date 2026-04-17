using System.ComponentModel.DataAnnotations;

namespace ElearningAPI.DTOs
{
    public class QuestionCreateDTO
    {
        [Required]
        public int QuizId { get; set; }

        [Required]
        public string QuestionText { get; set; } = string.Empty;

        [Required]
        public string OptionA { get; set; } = string.Empty;

        [Required]
        public string OptionB { get; set; } = string.Empty;

        [Required]
        public string OptionC { get; set; } = string.Empty;

        [Required]
        public string OptionD { get; set; } = string.Empty;

        [Required]
        [RegularExpression("A|B|C|D", ErrorMessage = "CorrectAnswer must be A, B, C, or D")]
        public string CorrectAnswer { get; set; } = string.Empty;
    }
}