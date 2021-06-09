-- Module 15: list records with same score

SELECT score FROM second_table COUNT(score) as 'number' GROUP BY score ORDER BY number DESC;
