-- Display the top 3 cities temperature
-- Display the highest temperature for 3 cities between July and August ordered by temperature
SELECT city, AVG(value) AS avg_temp FROM `temperatures` WHERE `month` BETWEEN 7 AND 8 GROUP BY `city` ORDER BY AVG(value) desc LIMIT 3;
