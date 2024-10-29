import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PostgesConfig:
    url: str


def env_var_by_key(key: str) -> str:
    """
    Returns value from env vars by key
    if value exists, otherwise raises
    Exception.
    """
    value = os.getenv(key)
    if not value:
        message = f"Env var {key} doesn't exist"
        raise Exception(message)
    return value


def postgres_config_from_env() -> PostgesConfig:
    db_name = env_var_by_key("POSTGRES_DB")
    db_password = env_var_by_key("POSTGRES_PASSWORD")
    db_host = env_var_by_key("POSTGRES_HOST")
    db_port = env_var_by_key("POSTGRES_PORT")
    db_user = env_var_by_key("POSTGRES_USER")

    return PostgesConfig(
        f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
