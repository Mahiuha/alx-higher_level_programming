-- List by best TV show genre
-- ^
SELECT g.name, SUM(r.rate) AS rating
FROM tv_genres g INNER JOIN tv_show_genres sg
  ON g.id = sg.genre_id
  INNER JOIN tv_show_ratings r
  ON sg.show_id = r.show_id
GROUP BY g.name
ORDER BY SUM(r.rate) desc;
