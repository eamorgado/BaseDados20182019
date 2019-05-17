
select Name from Region R;
select Name from CUSTPMER where Country in (select Name from COUNTRY where RegionId in(select RegionId from REGION));




select R.Name,C.Name from COUNTRY C,REGION R where C.RegionId=R.RegionId order by R.Name,C.Name;

