import duckdb
import plotly.express as px
import pandas as pd

# Connect to DuckDB
conn = duckdb.connect('../dev.duckdb')

# Load data
volume_by_region = conn.execute("SELECT * FROM main.volume_by_region").df()
revenue_by_region = conn.execute("SELECT * FROM main.revenue_by_region").df()
monthly_sales_revenue = conn.execute("SELECT * FROM main.monthly_sales_by_region").df()

pd.set_option('display.float_format', '{:,.2f}'.format)
#print(volume_by_region)
#print(revenue_by_region)
#print(monthly_sales_revenue)

region_colors = {
    'ASIA': '#636EFA',
    'MIDDLE EAST': '#EF553B',
    'AFRICA': '#00CC96',
    'EUROPE': '#AB63FA',
    'AMERICA': '#FFA15A'
}

# 1. Total Orders by Region
fig1 = px.bar(
    volume_by_region,
    x='region_name',
    y='total_orders',
    title='Total Orders by Region (2023)',
    color='region_name',
    color_discrete_map=region_colors,
    labels={'region_name': 'Region', 'total_orders': 'Total Orders'}
)
fig1.update_layout(yaxis_range=[39000, 41000])
fig1.update_traces(texttemplate='%{y:,.0f}', textposition='outside')
fig1.write_html("../analyses/volume_by_region.html")


# 2. Total Revenue by Region
fig2 = px.bar(
    revenue_by_region,
    x='region_name',
    y='total_revenue',
    title='Total Revenue by Region (2023)',
    color='region_name',
    color_discrete_map=region_colors,
    labels={'region_name': 'Region', 'total_revenue': 'Total Revenue ($)'}
)
fig2.update_layout(yaxis_range=[5700000000, 6300000000])
fig2.update_traces(texttemplate='$%{y:,.0f}', textposition='outside')
fig2.write_html("../analyses/revenue_by_region.html")

# 3. Average Order Value by Region
fig3 = px.bar(
    revenue_by_region,
    x='region_name',
    y='avg_order_value',
    title='Average Order Value by Region (2023)',
    color='region_name',
    color_discrete_map=region_colors,
    labels={'region_name': 'Region', 'avg_order_value': 'Avg Order Value ($)'}
)
fig3.update_traces(texttemplate='$%{y:,.0f}', textposition='outside')
fig3.update_layout(yaxis_range=[150000, 152000])
fig3.write_html("../analyses/avg_order_value_by_region.html")
fig3.show()

# 4. Monthly Orders by Region
fig4 = px.line(
    monthly_sales_revenue,
    x='order_month',
    y='total_orders',
    color='region_name',
    color_discrete_map=region_colors,
    title='Monthly Orders by Region (2023)',
    labels={'order_month': 'Month', 'total_orders': 'Total Orders', 'region_name': 'Region'}
)

fig4.update_traces(mode='lines+markers')
fig4.update_layout(yaxis_range=[3000, 3600])
fig4.write_html("../analyses/monthly_orders_by_region.html")

# 5. Monthly Revenue by Region
fig5 = px.line(
    monthly_sales_revenue,
    x='order_month',
    y='total_revenue',
    color='region_name',
    color_discrete_map=region_colors,
    title='Monthly Revenue by Region (2023)',
    labels={'order_month': 'Month', 'total_revenue': 'Total Revenue ($)', 'region_name': 'Region'}
)

fig5.update_traces(mode='lines+markers')
fig5.update_layout(yaxis_range=[450000000, 550000000])
fig5.write_html("../analyses/monthly_revenue_by_region.html")


fig1.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()

conn.close()