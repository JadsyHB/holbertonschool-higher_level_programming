-- Module 103: display max temp

SELECT state, MAX(value) as "max_temp" FROM temperatures ORDER BY state;
