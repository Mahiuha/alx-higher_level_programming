-- List all shows without a certain genre
-- List all shows that arent tagged with comedy
SELECT s.title
FROM tv_shows s
WHERE s.title NOT IN (SELECT s.title
                      FROM tv_shows s INNER JOIN tv_show_genres sg
                        ON s.id = sg.show_id
                        INNER JOIN tv_genres g
                        ON sg.genre_id = g.id
                      WHERE g.name = 'Comedy')
ORDER BY s.title;
