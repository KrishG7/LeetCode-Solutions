# Write your MySQL query statement below
SELECT s1.id
FROM Weather s1, Weather s2
WHERE s1.temperature > s2.temperature
AND DATEDIFF(s1.recordDate, s2.recordDate) = 1;
