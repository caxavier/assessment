select 
    r.region_name,
    sum(o.total_price) as total_revenue,
    round(sum(o.total_price) / count(o.order_key), 2) as avg_order_value
from {{ ref('stg_orders') }} o
left join {{ ref('stg_regions') }} r
on o.region_key = r.region_key
group by r.region_name
order by total_revenue desc