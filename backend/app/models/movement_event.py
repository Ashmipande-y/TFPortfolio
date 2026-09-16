from datetime import datetime
from enum import Enum
from uuid import UUID

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class MovementEventType(str, Enum):
    ENTRY = "entry"
    EXIT = "exit"
    TRANSFER = "transfer"
    CHECK_IN = "check_in"
    CHECK_OUT = "check_out"


class MovementEvent(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "movement_events"

    asset_id: Mapped[UUID] = mapped_column(
        ForeignKey("assets.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    location_id: Mapped[UUID] = mapped_column(
        ForeignKey("locations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    from_zone_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("zones.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    to_zone_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("zones.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    gate_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("gates.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    event_type: Mapped[MovementEventType] = mapped_column(
        SQLEnum(MovementEventType, name="movement_event_type"),
        nullable=False,
    )

    triggered_by: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    event_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    device_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("devices.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    idempotency_key: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )

    event_metadata: Mapped[dict | None] = mapped_column(
        "metadata",
        JSONB,
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )