from typing import TYPE_CHECKING
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from core.models import Base
from core.models.mixins.int_id_pk import IntIdPkMixin
from core.types.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(
    Base,
    IntIdPkMixin,
    SQLAlchemyBaseUserTable[UserIdType],
):
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
