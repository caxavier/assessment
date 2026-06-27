select 
    R_REGIONKEY as region_key,
    R_NAME as region_name,
    R_COMMENT as region_comment
from {{ ref('REGIONS') }}