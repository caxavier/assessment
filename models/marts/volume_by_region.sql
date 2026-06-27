select 
    r.region_name,
    count(o.order_key) as total_orders
from {{ ref('stg_orders') }} o
left join {{ ref('stg_regions') }} r
on o.region_key = r.region_key
group by r.region_name
order by total_orders desc