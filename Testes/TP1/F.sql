select Title,sum(Charge) from MOVIE natural join STREAM natural join MOVIE_GENRE natural join GENRE where Label like 'Action' group by 1 order by 2 desc,1 limit 20;
