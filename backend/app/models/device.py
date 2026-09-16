from enum import Enum
from uuid import UUID

from sqlalchemy import Boolean, Enum as SQLEnum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class DeviceType(str, Enum):
    QR_SCANNER = "qr_scanner"
    RFID_READER = "rfid_reader"
    GATE_CONTROLLER = "gate_controller"
    ANPR_CAMERA = "anpr_camera"
    IOT_SENSOR = "iot_sensor"


class Device(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "devices"

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

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    device_uid: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )

    device_type: Mapped[DeviceType] = mapped_column(
        SQLEnum(DeviceType, name="device_type"),
        nullable=False,
        index=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true",
    )