-- Group by column(s) in a table
-- Lists the number of records the with same score in the table `second_table`
SELECT score , COUNT(score) AS number FROM `second_table` GROUP BY score ORDER BY score desc;
