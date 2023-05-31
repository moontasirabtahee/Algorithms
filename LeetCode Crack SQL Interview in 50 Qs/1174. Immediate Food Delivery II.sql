

select
    round(sum(if(order_date=customer_pref_delivery_date,1,0))/count(distinct customer_id)*100,2)
    immediate_percentage
from Delivery
where (customer_id, order_date) in
            (select customer_id, min(order_date)
            from Delivery
            group by customer_id);