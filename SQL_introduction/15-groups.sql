-- lists the number of records with the same score in second_table
SELECT score, COUNT(score) as number
ORDER BY number;
