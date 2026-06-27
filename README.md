# Sales Analytics Assessment

## Overview
This project analyzes sales data across different regions using dbt and DuckDB.
It includes data transformation models and Python visualizations to answer:
- Which region had the highest sales volume and revenue?
- What trends and patterns exist in the data?

## Project Structure

    assessment/
    ├── models/
    │   ├── staging/
    │   │   ├── stg_orders.sql              # Cleaned orders data
    │   │   └── stg_regions.sql             # Cleaned regions data
    │   └── marts/
    │       ├── volume_by_region.sql        # Total orders by region
    │       ├── revenue_by_region.sql       # Total revenue by region
    │       └── monthly_sales_by_region.sql # Monthly breakdown by region
    ├── seeds/
    │   ├── ORDERS.csv
    │   └── REGIONS.csv
    ├── analyses/
    │   └── visualizations.py              # Plotly charts
    └── dbt_project.yml

## Requirements
- Python 3.12+
- dbt-duckdb

## Setup & Run

### 1. Install dependencies
```bash
pip install dbt-duckdb plotly pandas duckdb
```

### 2. Load raw data
```bash
dbt seed
```

### 3. Run transformations
```bash
dbt run
```

### 4. Run tests
```bash
dbt test
```

### 5. Generate visualizations
```bash
cd analyses
python visualizations.py
```

## Key Findings
- **ASIA** leads in both total orders (40,339) and total revenue ($6.1B)
- **AFRICA** ranks 3rd in volume but last in revenue, suggesting lower average order value ($150k)
- **AMERICA** ranks last in volume but 3rd in revenue, suggesting higher average order value ($151k)
- **February** is consistently the weakest month across all regions
- **March, May, July and December** show peaks in activity