from datetime import datetime
from enum import Enum
from uuid import UUID

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, UUIDPrimaryKeyMixin


class GatePassType(str, Enum):
    ENTRY = "entry"
    EXIT = "exit"
    DELIVERY = "delivery"
    TRANSFER = "transfer"


class GatePassStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    USED = "used"
    EXPIRED = "expired"
    CANCELLED = "cancelled"


class GatePass(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "gate_passes"

    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    location_id: Mapped[UUID] = mapped_column(
        ForeignKey("locations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    gate_id: Mapped[UUID] = mapped_column(
        ForeignKey("gates.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    vehicle_id: Mapped[UUID] = mapped_column(
        ForeignKey("vehicles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    pass_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True,
    )

    pass_type: Mapped[GatePassType] = mapped_column(
        SQLEnum(GatePassType, name="gate_pass_type"),
        nullable=False,
    )

    status: Mapped[GatePassStatus] = mapped_column(
        SQLEnum(GatePassStatus, name="gate_pass_status"),
        nullable=False,
        default=GatePassStatus.PENDING,
        server_default=GatePassStatus.PENDING.name,
    )

    valid_from: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    valid_until: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    purpose: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_by: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=False,
        index=True,
    )

    approved_by: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )