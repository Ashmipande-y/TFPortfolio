from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, UUIDPrimaryKeyMixin


class GatePassAsset(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "gate_pass_assets"

    gate_pass_id: Mapped[UUID] = mapped_column(
        ForeignKey("gate_passes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    asset_id: Mapped[UUID] = mapped_column(
        ForeignKey("assets.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint(
            "gate_pass_id",
            "asset_id",
            name="uq_gate_pass_asset",
        ),
    )