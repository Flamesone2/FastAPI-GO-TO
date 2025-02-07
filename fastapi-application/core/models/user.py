from collections.abc import AsyncGenerator
from typing import TYPE_CHECKING

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from core.models import Base
from core.models.mixins.int_id_pk import IntIdPkMixin
from core.types.user_id import UserId_type

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(
    Base,
    IntIdPkMixin,
    SQLAlchemyBaseUserTable[UserId_type],
):
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
