# Write your MySQL query statement below
SELECT 
    s1.firstName, 
    s1.lastName, 
    s2.city, 
    s2.state 
FROM Person s1 
LEFT JOIN Address s2 ON s1.personId = s2.personId;
