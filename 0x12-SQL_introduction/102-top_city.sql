-- Module 102

SELECT city, AVG(value) as 'avg_temp'
FROM temperatures
ORDER BY avg_temp DESC LIMIT 3
GROUP BY city
WHERE `month`=7 OR `month`=8;
