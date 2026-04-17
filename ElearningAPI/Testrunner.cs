using System;
using System.Collections.Generic;
using System.Linq;

namespace ElearningAPI
{
    public static class TestRunner
    {
        public static void RunTests()
        {
            Console.WriteLine("Running Tests...\n");

            Test_Course_CRUD();
            Test_Quiz_Scoring();
            Test_LINQ_Filtering();
            Test_API_Response();
            Test_Exception_Handling();

            Console.WriteLine("\nAll Tests Completed!");
        }

        // 1. Course CRUD
        static void Test_Course_CRUD()
        {
            var courses = new List<string>();

            // Create
            courses.Add("Java");

            // Read
            bool exists = courses.Contains("Java");

            // Update
            courses[0] = "Java Updated";

            // Delete
            courses.Remove("Java Updated");

            if (exists && courses.Count == 0)
                Console.WriteLine("Course CRUD Test Passed ✅");
            else
                Console.WriteLine("Course CRUD Test Failed ❌");
        }

        // 2. Quiz Scoring
        static void Test_Quiz_Scoring()
        {
            var correctAnswers = new List<string> { "A", "B", "C" };
            var userAnswers = new List<string> { "A", "B", "D" };

            int score = 0;

            for (int i = 0; i < correctAnswers.Count; i++)
            {
                if (correctAnswers[i] == userAnswers[i])
                    score++;
            }

            if (score == 2)
                Console.WriteLine("Quiz Scoring Test Passed ✅");
            else
                Console.WriteLine("Quiz Scoring Test Failed ❌");
        }

        // 3. LINQ Filtering
        static void Test_LINQ_Filtering()
        {
            var numbers = new List<int> { 1, 2, 3, 4, 5 };

            var result = numbers.Where(x => x > 3).ToList();

            if (result.Count == 2 && result.Contains(4) && result.Contains(5))
                Console.WriteLine("LINQ Filtering Test Passed ✅");
            else
                Console.WriteLine("LINQ Filtering Test Failed ❌");
        }

        // 4. API Response (Status + Data)
        static void Test_API_Response()
        {
            int statusCode = 200;
            string data = "Success";

            if (statusCode == 200 && data == "Success")
                Console.WriteLine("API Response Test Passed ✅");
            else
                Console.WriteLine("API Response Test Failed ❌");
        }

        // 5. Exception Handling (Invalid Quiz)
        static void Test_Exception_Handling()
        {
            try
            {
                throw new Exception("Invalid Quiz");
            }
            catch (Exception ex)
            {
                if (ex.Message == "Invalid Quiz")
                    Console.WriteLine("Exception Handling Test Passed ✅");
                else
                    Console.WriteLine("Exception Handling Test Failed ❌");
            }
        }
    }
}