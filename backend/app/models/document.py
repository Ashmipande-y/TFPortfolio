from datetime import datetime
from enum import Enum
from uuid import UUID

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, UUIDPrimaryKeyMixin


class DocumentType(str, Enum):
    CHALLAN = "challan"
    INVOICE = "invoice"
    PURCHASE_ORDER = "purchase_order"
    GATE_PASS = "gate_pass"
    EVIDENCE = "evidence"


class Document(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "documents"

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

    asset_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("assets.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    gate_pass_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("gate_passes.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    document_type: Mapped[DocumentType] = mapped_column(
        SQLEnum(DocumentType, name="document_type"),
        nullable=False,
        index=True,
    )

    file_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    storage_key: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    mime_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    uploaded_by: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )