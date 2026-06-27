select 
    strftime(date_trunc('month', o.order_date), '%b/%Y') as order_month,
    r.region_name,
    count(o.order_key) as total_orders,
    sum(o.total_price) as total_revenue
from {{ ref('stg_orders') }} o
left join {{ ref('stg_regions') }} r
on o.region_key = r.region_key
group by r.region_name, date_trunc('month', o.order_date)
order by date_trunc('month', o.order_date), total_orders desc 