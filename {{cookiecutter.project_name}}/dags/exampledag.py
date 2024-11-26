from airflow.decorators import dag
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig
from pendulum import datetime
import os
import sys

# This is mandatory, as AIRFLOW runs the DAGs from `tmp` directory
airflow_home = os.environ['AIRFLOW_HOME']
sys.path.append(airflow_home)

profile_config = ProfileConfig( 
    profile_name="{{ cookiecutter.project_name }}", 
    target_name="{{ cookiecutter.project_name }}", 
    profiles_yml_filepath=f"../{{cookiecutter.dbt_project_name}}/.dbt/profiles.yml"
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
        project_config=ProjectConfig(DBT_PROJECT_DIR,),
        profile_config=profile_config,
        operator_args={ 
            "install_deps": True, 
        }, 
        default_args=default_args,
    )

example_pipeline()
