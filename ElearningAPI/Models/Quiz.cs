using System.Collections.Generic;

namespace ElearningAPI.Models
{
    public class Quiz
    {
        public int QuizId { get; set; }
        public int CourseId { get; set; }

        public string Title { get; set; } = string.Empty;

        public Course Course { get; set; } = null!;
        public List<Question> Questions { get; set; } = new();
    }
}