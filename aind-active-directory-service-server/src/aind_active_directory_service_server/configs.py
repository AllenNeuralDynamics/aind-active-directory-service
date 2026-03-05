"""Module for settings to connect to backend"""

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
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
    domain: str = Field("corp.alleninstitute.org", description="Domain to connect to")


settings = Settings()
