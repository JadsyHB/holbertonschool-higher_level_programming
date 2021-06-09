-- Module 15: list records with same score

SELECT score FROM second_table COUNT(*) as number GROUP BY score DESC;
