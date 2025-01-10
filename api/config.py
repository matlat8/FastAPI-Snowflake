from functools import lru_cache
from pydantic_settings import BaseSettings
from typing import Optional

class Config(BaseSettings):
    app_name: str = "FastAPI Snowflake"
    environment: str = "dev"
    snowflake_user: str
    snowflake_password: str
    snowflake_account: str
    snowflake_database: Optional[str] = "DEMO_DB" # I like to specify the full path to the data
    snowflake_schema: Optional[str] = "PUBLIC"    # table in queries so these feel optional to me
    snowflake_warehouse: Optional[str] = "COMPUTE_WH"
    
@lru_cache()
def get_settings():
    return Config()

settings = get_settings()