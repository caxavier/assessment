with orders as (
    select 
        O_ORDERKEY as order_key,
        O_CUSTKEY as customer_key,
        O_REGIONKEY as region_key,
        O_ORDERSTATUS as order_status,
        cast(replace(O_TOTALPRICE, ',', '.') as decimal(15, 2)) as total_price,
        strptime(O_ORDERDATE, '%d/%m/%Y') as order_date,
        O_ORDERPRIORITY as order_priority,
        O_CLERK as clerk,
        O_SHIPPRIORITY as ship_priority,
        O_COMMENT as comment
    from {{ ref('ORDERS') }}
)

select *
from orders
where order_date >= (select  max(order_date) from orders) - interval '{{ var("months_back") }}' months
