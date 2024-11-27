from airflow.decorators import dag
from cosmos import DbtTaskGroup, ExecutionConfig, ProjectConfig, ProfileConfig
from pendulum import datetime
import os
import sys

# This is mandatory, as AIRFLOW runs the DAGs from `tmp` directory
AIRFLOW_PATH = "/usr/local/airflow"
sys.path.append(AIRFLOW_PATH)

profile_config = ProfileConfig( 
    profile_name="{{ cookiecutter.dbt_project_name }}", 
    target_name="{{ cookiecutter.profile_target }}", 
    profiles_yml_filepath=f"{AIRFLOW_PATH}/dbt/.dbt/.profiles.yml"
)

default_args = {
    "owner": "Astro",
    "retries": 1,
}

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@hourly",
    catchup=False,
    doc_md=__doc__,
    default_args=default_args,
    tags=["dbt"],
)
def example_pipeline():
    transform_data = DbtTaskGroup(
        group_id="transform_data",
        project_config=ProjectConfig(
            dbt_project_path=f"{AIRFLOW_PATH}/dbt",
        ),
        profile_config=profile_config,
        execution_config=ExecutionConfig(
            dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",
        ),
        operator_args={ 
            "install_deps": True,  # required to install dbt dependencies
        }, 
        default_args=default_args,
    )

    transform_data

example_pipeline()
