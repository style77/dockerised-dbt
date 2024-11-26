
-- Use the `ref` function to select from other models

select *
from {% raw %}{{ ref('my_first_dbt_model') }}{% endraw %}
where id = 1
