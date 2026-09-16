from enum import Enum
from uuid import UUID

from sqlalchemy import Boolean, Enum as SQLEnum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class UserRole(str, Enum):
    ADMIN = "admin"
    SITE_MANAGER = "site_manager"
    SECURITY = "security"
    SUPERVISOR = "supervisor"
    VIEWER = "viewer"


class User(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "users"

    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(320),
        nullable=False,
        unique=True,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole, name="user_role"),
        nullable=False,
        default=UserRole.VIEWER,
        server_default=UserRole.VIEWER.name,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true",
    )