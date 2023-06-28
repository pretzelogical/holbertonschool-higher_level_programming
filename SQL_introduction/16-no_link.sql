-- lists all records of second_table in hbtn_0c_0
SELECT (score, name) FROM second_table
WHERE EXISTS (SELECT (name) FROM second_table)
ORDER BY score DESC;
