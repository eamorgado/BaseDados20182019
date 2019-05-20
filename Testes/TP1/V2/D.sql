select Title, count(*) from MOVIE natural join STREAM group by Title order by count(*) desc,Title;
