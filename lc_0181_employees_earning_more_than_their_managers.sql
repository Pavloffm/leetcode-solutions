SELECT e1.name as Employee
FROM Employee AS e1
JOIN Employee AS e2 ON e1.managerId = e2.id
WhERE e1.salary > e2.salary
