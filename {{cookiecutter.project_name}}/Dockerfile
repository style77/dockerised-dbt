FROM quay.io/astronomer/astro-runtime:12.4.0

USER $AIRFLOW_UID

WORKDIR /usr/local/airflow

RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir -r ./requirements.txt && deactivate