


Select r.contest_id ,
round(count(r.user_id)/(select count(*) from Users)*100,2)
as percentage
from Users u , Register r
where u.user_id = r.user_id
group by r.contest_id
order by percentage desc , contest_id asc