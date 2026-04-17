
-- DATABASE

USE ElearningDB;

-- BASIC QUERIES (SELECT, WHERE, ORDER BY)

-- SELECT
SELECT * FROM Users;

-- WHERE
SELECT * FROM Results
WHERE Score > 5;

-- ORDER BY
SELECT * FROM Results
ORDER BY Score DESC;

-- JOINS (INNER JOIN + LEFT JOIN)


-- INNER JOIN
SELECT u.FullName, r.Score
FROM Users u
INNER JOIN Results r ON u.UserId = r.UserId;

-- LEFT JOIN
SELECT u.FullName, r.Score
FROM Users u
LEFT JOIN Results r ON u.UserId = r.UserId;

-- AGGREGATION (GROUP BY, COUNT, AVG)

-- COUNT
SELECT UserId, COUNT(*) AS TotalAttempts
FROM Results
GROUP BY UserId;

-- AVG
SELECT UserId, AVG(Score) AS AvgScore
FROM Results
GROUP BY UserId;

-- SUBQUERY (Above Average Users)


SELECT * FROM Results
WHERE Score > (
    SELECT AVG(Score) FROM Results
);

-- SET OPERATORS (UNION)


SELECT FullName AS Name FROM Users
UNION
SELECT Title FROM Courses;


-- DML OPERATIONS (INSERT, UPDATE, DELETE)


-- INSERT
INSERT INTO Results (UserId, QuizId, Score, AttemptDate)
VALUES (1, 1, 10, GETDATE());

-- UPDATE
UPDATE Results
SET Score = 8
WHERE ResultId = 1;

-- DELETE
DELETE FROM Results
WHERE ResultId = 1;