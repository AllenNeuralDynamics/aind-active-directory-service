"""Module to handle endpoint responses"""

from fastapi import APIRouter, HTTPException, status
from fastapi_cache.decorator import cache

from ms_active_directory import ADDomain

from aind_active_directory_service_server.models import HealthCheck, UserInfo
from aind_active_directory_service_server.configs import settings

router = APIRouter()


@router.get(
    "/healthcheck",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    """
    ## Endpoint to perform a healthcheck on.

    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck()


@router.get(
    "/user_info/{username}",
    response_model=UserInfo,
)
@cache(expire=86400)
async def get_user_from_active_directory(username: str) -> UserInfo:
    """Queries active directory for user information

    Params:
        username (str): user login or full name

    Returns:
        UserInfo: user information from Active Directory
    """
    domain = ADDomain(settings.domain)
    ad_session = domain.create_session_as_user(
        settings.username,
        settings.password.get_secret_value(),
    )
    ad_user = ad_session.find_user_by_name(
        username, attributes_to_lookup=["mail"]
    )
    if ad_user is None:
        raise HTTPException(
            status_code=404,
            detail=f"User {username} not found in the institute Active Directory",
        )
    return UserInfo(
        username=ad_user.samaccount_name,
        full_name=ad_user.common_name,
        email=ad_user.all_attributes["mail"],
    )
