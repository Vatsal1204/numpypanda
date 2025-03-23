CREATE DATABASE ECommerceDB;
USE ECommerceDB;

-- Customers Table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    City VARCHAR(50)
);

-- Orders Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    Total DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Products Table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(50),
    Price DECIMAL(10,2)
);

-- OrderDetails Table
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
-- Customers (Added New York for Q7)
INSERT INTO Customers VALUES
(1, 'John Sharma', 28, 'Mumbai'),
(2, 'Priya Verma', 35, 'New York'),
(3, 'Raj Patel', 22, 'Delhi'),
(4, 'Anjali Kapoor', 40, 'New York');

-- Products
INSERT INTO Products VALUES
(101, 'Wireless Headphones', 2500.00),
(102, 'Smart Watch', 850.50),
(103, 'E-Reader', 450.75),
(104, 'Bluetooth Speaker', 299.99),
(105, 'Gaming Console', 4200.00);

-- Orders (Added more orders for Q6)
INSERT INTO Orders VALUES
(1001, '2023-01-15', 1, 5350.00),
(1002, '2023-02-20', 1, 1350.49),
(1003, '2023-03-10', 1, 299.99),
(1004, '2023-04-05', 1, 850.50),
(1005, '2023-05-12', 1, 4200.00),
(1006, '2023-06-18', 1, 999.99),
(1007, '2022-12-05', 3, 850.50);

-- OrderDetails
INSERT INTO OrderDetails VALUES
(1, 1001, 101, 2),
(2, 1001, 105, 1),
(3, 1002, 103, 3),
(4, 1003, 104, 1),
(5, 1004, 102, 1),
(6, 1005, 105, 1),
(7, 1006, 101, 2);

-- 1. Names and cities of all customers
SELECT Name, City FROM Customers;

-- 2. Total amount spent per customer
SELECT c.Name, SUM(o.Total) AS TotalSpent
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.Name;

-- 3. 2023 monthly orders
SELECT 
    MONTH(OrderDate) AS Month,
    COUNT(OrderID) AS OrderCount
FROM Orders
WHERE YEAR(OrderDate) = 2023
GROUP BY MONTH(OrderDate);

-- 4. Top 3 expensive products
SELECT Name, Price 
FROM Products
ORDER BY Price DESC
LIMIT 3;

-- 5. Full order details
SELECT 
    o.OrderID,
    o.OrderDate,
    c.Name AS CustomerName,
    o.Total
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID;

-- 6. Customers with >5 orders
SELECT c.Name, COUNT(o.OrderID) AS OrderCount
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID
HAVING COUNT(o.OrderID) > 5;  -- Fixed from original

-- 7. Average age in New York
SELECT AVG(Age) AS AverageAge
FROM Customers
WHERE City = 'New York';  -- Fixed city filter

-- 8. Never ordered products
SELECT p.Name
FROM Products p
LEFT JOIN OrderDetails od ON p.ProductID = od.ProductID
WHERE od.OrderDetailID IS NULL;

-- 9. No 2023 orders
SELECT c.Name
FROM Customers c
LEFT JOIN Orders o 
    ON c.CustomerID = o.CustomerID
    AND YEAR(o.OrderDate) = 2023
WHERE o.OrderID IS NULL;

-- 10. Product sales quantities
SELECT 
    p.Name,
    COALESCE(SUM(od.Quantity), 0) AS TotalSold
FROM Products p
LEFT JOIN OrderDetails od ON p.ProductID = od.ProductID
GROUP BY p.ProductID, p.Name;