-- List average temperatures
-- Display average temperature in Fahreheit by city ordered by temperature in descending order
SELECT city, AVG(value) AS avg_temp FROM `temperatures` GROUP BY `city` ORDER BY AVG(value) desc;
