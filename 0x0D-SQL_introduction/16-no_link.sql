-- Do not list rows with NULL column
-- List rows only where `name` is not NULL
SELECT score, name FROM `second_table` WHERE NAME IS NOT NULL ORDER BY score desc;
