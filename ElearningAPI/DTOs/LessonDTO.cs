using System.ComponentModel.DataAnnotations;

namespace ElearningAPI.DTOs
{
    public class LessonDTO
    {
        public int LessonId { get; set; }

        [Required]
        public int CourseId { get; set; }

        [Required]
        public string Title { get; set; } = string.Empty;

        [Required]
        public string Content { get; set; } = string.Empty;

        public int OrderIndex { get; set; }
    }
}