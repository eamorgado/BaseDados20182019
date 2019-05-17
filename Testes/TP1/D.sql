select Title, count(*) streams from MOVIE natural join STREAM group by Title order by count(*) desc,Title;
