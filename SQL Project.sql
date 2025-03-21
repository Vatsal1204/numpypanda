-- =============================================
-- STEP 1: CREATE DATABASE & TABLES
-- =============================================
CREATE DATABASE IndianUniversityDB;
USE IndianUniversityDB;

-- Departments Table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

-- Students Table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    EnrollmentDate DATE
);

-- Courses Table
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    DepartmentID INT,
    Credits INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Instructors Table (with Salary)
CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT,
    Salary DECIMAL(10,2),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Enrollments Table
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- =============================================
-- STEP 2: INSERT SAMPLE DATA (INDIAN NAMES)
-- =============================================
-- Departments
INSERT INTO Departments VALUES
(1, 'Computer Science'),
(2, 'Mathematics'),
(3, 'Sanskrit');

-- Students
INSERT INTO Students VALUES
(1, 'Aarav', 'Patel', 'aarav@email.com', '2023-01-15'),
(2, 'Priya', 'Sharma', 'priya@email.com', '2021-08-01'),
(3, 'Rohan', 'Singh', 'rohan@email.com', '2023-06-10');

-- Courses
INSERT INTO Courses VALUES
(101, 'Introduction to SQL', 1, 3),
(102, 'Data Structures', 1, 4),
(201, 'Vedic Mathematics', 2, 4);

-- Instructors
INSERT INTO Instructors VALUES
(1, 'Rajesh', 'Verma', 1, 95000.00),
(2, 'Anika', 'Choudhary', 2, 87000.00);

-- Enrollments
INSERT INTO Enrollments VALUES
(1, 1, 101, '2023-01-20'),
(2, 1, 102, '2023-01-20'),
(3, 3, 201, '2023-06-15');

-- =============================================
-- STEP 3: ANSWER ALL 16 QUESTIONS BELOW
-- =============================================

-- 1. CRUD Operations (Create, Read, Update, Delete)
-- Create (Insert)
INSERT INTO Students VALUES (4, 'Neha', 'Gupta', 'neha@email.com', '2024-01-01');

-- Read (Select)
SELECT * FROM Students;

-- Update
UPDATE Students SET Email = 'aarav.new@email.com' WHERE StudentID = 1;

-- Delete
DELETE FROM Enrollments WHERE EnrollmentID = 3;

-- 2. Students enrolled after 2022
SELECT * FROM Students 
WHERE YEAR(EnrollmentDate) > 2022;

-- 3. Mathematics courses (limit 5)
SELECT * FROM Courses 
WHERE DepartmentID = 2 
LIMIT 5;

-- 4. Courses with >5 students
SELECT CourseID, COUNT(StudentID) AS TotalStudents
FROM Enrollments
GROUP BY CourseID
HAVING TotalStudents > 5;

-- 5. Students in both SQL & Data Structures
SELECT s.* FROM Students s
WHERE s.StudentID IN (SELECT StudentID FROM Enrollments WHERE CourseID = 101)
AND s.StudentID IN (SELECT StudentID FROM Enrollments WHERE CourseID = 102);

-- 6. Students in either SQL or Data Structures
SELECT DISTINCT s.* FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
WHERE e.CourseID IN (101, 102);

-- 7. Average course credits
SELECT AVG(Credits) AS AverageCredits FROM Courses;

-- 8. Max salary in Computer Science
SELECT MAX(Salary) AS MaxSalary
FROM Instructors
WHERE DepartmentID = 1;

-- 9. Students per department
SELECT d.DepartmentName, COUNT(DISTINCT e.StudentID) AS TotalStudents
FROM Enrollments e
JOIN Courses c ON e.CourseID = c.CourseID
JOIN Departments d ON c.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName;

-- 10. INNER JOIN: Students & Courses
SELECT s.FirstName, c.CourseName
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
JOIN Courses c ON e.CourseID = c.CourseID;

-- 11. LEFT JOIN: All students (even unenrolled)
SELECT s.FirstName, c.CourseName
FROM Students s
LEFT JOIN Enrollments e ON s.StudentID = e.StudentID
LEFT JOIN Courses c ON e.CourseID = c.CourseID;

-- 12. Courses with >10 students (Subquery)
SELECT * FROM Students
WHERE StudentID IN (
    SELECT StudentID FROM Enrollments
    WHERE CourseID IN (
        SELECT CourseID FROM Enrollments
        GROUP BY CourseID
        HAVING COUNT(StudentID) > 10
    )
);

-- 13. Extract enrollment year
SELECT EnrollmentID, YEAR(EnrollmentDate) AS Year
FROM Enrollments;

-- 14. Instructor full names
SELECT CONCAT(FirstName, ' ', LastName) AS FullName
FROM Instructors;

-- 15. Running total of enrollments
SELECT EnrollmentDate, 
       SUM(COUNT(*)) OVER (ORDER BY EnrollmentDate) AS RunningTotal
FROM Enrollments
GROUP BY EnrollmentDate;

-- 16. Senior/Junior students
SELECT FirstName,
       CASE
           WHEN EnrollmentDate < '2020-01-01' THEN 'Senior'
           ELSE 'Junior'
       END AS Status
FROM Students;