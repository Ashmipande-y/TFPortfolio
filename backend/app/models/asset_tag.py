from datetime import datetime
from enum import Enum
from uuid import UUID

from sqlalchemy import Boolean, DateTime, Enum as SQLEnum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, UUIDPrimaryKeyMixin


class AssetTagType(str, Enum):
    QR = "qr"
    RFID = "rfid"
    NFC = "nfc"


class AssetTag(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "asset_tags"

    asset_id: Mapped[UUID] = mapped_column(
        ForeignKey("assets.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    tag_uid: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )

    tag_type: Mapped[AssetTagType] = mapped_column(
        SQLEnum(AssetTagType, name="asset_tag_type"),
        nullable=False,
        default=AssetTagType.QR,
        server_default=AssetTagType.QR.name,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true",
    )

    revoked_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )