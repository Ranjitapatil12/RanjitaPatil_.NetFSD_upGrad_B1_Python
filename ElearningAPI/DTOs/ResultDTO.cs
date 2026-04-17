namespace ElearningAPI.DTOs
{
    public class ResultDTO
    {
        public int ResultId { get; set; }
        public int QuizId { get; set; }
        public int Score { get; set; }
        public DateTime AttemptDate { get; set; }
    }
}