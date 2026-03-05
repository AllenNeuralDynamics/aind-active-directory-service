"""Models and schema definitions for backend data structures"""

from typing import Literal

from pydantic import BaseModel, Field

from aind_active_directory_service_server import __version__


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: Literal["OK"] = "OK"
    service_version: str = __version__


class UserInfo(BaseModel):
    """Response model for user information from Active Directory."""

    username: str = Field(..., description="SAM account name of the user")
    full_name: str = Field(..., description="Common name of the user")
    email: str = Field(..., description="Email address of the user")
