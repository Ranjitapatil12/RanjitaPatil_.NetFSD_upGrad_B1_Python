using AutoMapper;
using ElearningAPI.Models;
using ElearningAPI.DTOs;

namespace ElearningAPI.Mappings
{
    public class MappingProfile : Profile
    {
        public MappingProfile()
        {
            // ✅ USER
            CreateMap<UserRegisterDTO, User>();
            CreateMap<UserUpdateDTO, User>();
            CreateMap<User, UserRegisterDTO>();

            // ✅ COURSE
            CreateMap<Course, CourseDTO>();
            CreateMap<CourseDTO, Course>();

            // ✅ LESSON
            CreateMap<Lesson, LessonDTO>();
            CreateMap<LessonDTO, Lesson>();

            // ✅ QUIZ
            CreateMap<Quiz, QuizDTO>();
            CreateMap<QuizCreateDTO, Quiz>();

            // ✅ QUESTION
            CreateMap<Question, QuestionDTO>();
            CreateMap<QuestionCreateDTO, Question>();

            // ✅ RESULT
            CreateMap<Result, ResultDTO>();
        }
    }
}