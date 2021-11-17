-- List all genres for a show
-- List all genres for Dexter
SELECT g.name AS name
FROM tv_shows s INNER JOIN tv_show_genres sg
  ON s.id = sg.show_id
INNER JOIN tv_genres g
  ON sg.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY g.name;
