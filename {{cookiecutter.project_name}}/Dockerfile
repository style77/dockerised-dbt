FROM quay.io/astronomer/astro-runtime:12.4.0

USER root

{% if cookiecutter.adapter == "postgres" %}
# In case DBT decide to use psycopg2 instead of psycopg2-binary :)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*
{% endif %}

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m venv dbt_venv && \
    source dbt_venv/bin/activate && \
    {% if cookiecutter.adapter == "postgres" %}DBT_PSYCOPG2_NAME=psycopg2-binary && {% endif %}\
    pip install --no-cache-dir dbt-core \
    {% if cookiecutter.adapter == "postgres" %}dbt-postgres{% elif cookiecutter.adapter == "snowflake" %}dbt-snowflake{% elif cookiecutter.adapter == "bigquery" %}dbt-bigquery{% endif %} && \
    deactivate