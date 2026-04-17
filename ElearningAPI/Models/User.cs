using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace ElearningAPI.Models
{
    public class User
    {
        public int UserId { get; set; }

        [Required]
        public string FullName { get; set; } = string.Empty;

        [Required]
        [EmailAddress]
        public string Email { get; set; } = string.Empty;

        [Required]
        public string PasswordHash { get; set; } = string.Empty;

        public DateTime CreatedAt { get; set; }

        [JsonIgnore]
        public List<Course> Courses { get; set; } = new();

        [JsonIgnore]
        public List<Result> Results { get; set; } = new();
    }
}