"""Module for settings to connect to backend"""

from typing import Optional
from pydantic import Field, SecretStr, RedisDsn
from pydantic_settings import SettingsConfigDict
from aind_settings_utils.aws import SecretsManagerBaseSettings

class Settings(SecretsManagerBaseSettings):
    """
    ### Settings needed to connect to the active directory.
    We will just connect to an example active directory.
    """

    model_config = SettingsConfigDict(env_prefix="AD_")
    username: str = Field(
        ..., description="Username to connect to the active directory"
    )
    password: SecretStr = Field(
        ..., description="Password to connect to the active directory"
    )
    domain: str = Field(..., description="Domain to connect to")
    redis_url: Optional[RedisDsn] = Field(
        None,
        description="Redis URL for caching (optional, defaults to in-memory cache)",
    )


settings = Settings()
