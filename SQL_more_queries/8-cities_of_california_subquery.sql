-- lists all cities of California that can be found in hbtn_0d_usa
SELECT id, name from cities
WHERE state_id IN
(SELECT id
FROM states
where name = "California")
ORDER BY id ASC;
