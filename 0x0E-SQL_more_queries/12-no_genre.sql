-- Lists shows with their genres
-- ^
SELECT s.title AS title, g.genre_id AS genre_id
FROM tv_shows s LEFT OUTER JOIN tv_show_genres g
  ON s.id = g.show_id
WHERE g.genre_id IS NULL
ORDER BY s.title, g.genre_id;
