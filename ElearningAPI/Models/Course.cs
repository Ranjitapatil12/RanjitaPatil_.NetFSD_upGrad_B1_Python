using System;
using System.Collections.Generic;

namespace ElearningAPI.Models
{
    public class Course
    {
        public int CourseId { get; set; }

        public string Title { get; set; } = string.Empty;

        public string Description { get; set; } = string.Empty;

        // ✅ FIX: use UserId (NOT CreatedBy)
        public int UserId { get; set; }

        public DateTime CreatedAt { get; set; }

        // Navigation
        public User? User { get; set; }

        public List<Lesson> Lessons { get; set; } = new();

        public List<Quiz> Quizzes { get; set; } = new();
    }
}