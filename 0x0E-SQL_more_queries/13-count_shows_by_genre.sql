-- Count number of shows a genre is linked to
-- ^
SELECT g.name AS genre, COUNT(gs.genre_id) AS number_of_shows
FROM tv_shows s INNER JOIN tv_show_genres gs
  ON s.id = gs.show_id
  INNER JOIN tv_genres g
  ON gs.genre_id = g.id
GROUP BY g.name
ORDER BY COUNT(gs.genre_id) desc;
