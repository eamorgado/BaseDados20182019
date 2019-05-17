select Name, count(*) from MOVIE natural join MOVIE_ACTOR natural join ACTOR group by 1 having count(*)>=15 order by 1;
