# from fastapi import APIRouter, Depends
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from core.models import db_helper
# from core.schemas.user import UserRead, UserCreate
# from crud.users import get_all_users, create_user
#
# router = APIRouter(tags=["Users"])
#
#
# @router.get("", response_model=list[UserRead])
# async def get_users(
#     session: AsyncSession = Depends(db_helper.session_getter),
# ):
#     users = await get_all_users(session=session)
#     return users
#
#
# @router.post("", response_model=UserRead)
# async def create_user(
#     user_create: UserCreate,
#     session: AsyncSession = Depends(db_helper.session_getter),
# ):
#     user = await create_user(session=session, user_create=user_create)
#     return user
from fastapi import APIRouter

from api.api_v1.fastapi_users_router import fastapi_users
from core.config import settings
from core.schemas.user import (
    UserRead,
    UserUpdate,
)

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
