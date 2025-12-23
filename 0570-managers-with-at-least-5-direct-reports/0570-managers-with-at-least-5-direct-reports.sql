# Write your MySQL query statement below
select e1.name FROM Employee as e1 JOIN Employee as e2 on e1.id=e2.managerId group by e1.id,e1.name HAVING count(e2.id)>=5; 
