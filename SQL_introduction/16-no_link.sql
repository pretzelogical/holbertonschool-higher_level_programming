-- lists all records of second_table in hbtn_0c_0
-- not listing rows without a name value
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
