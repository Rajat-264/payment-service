from sqlalchemy import Column, String, Float, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from enum import Enum as PyEnum

Base = declarative_base()

class PaymentStatus(str, PyEnum):
    Initiated = "Initiated"
    Success = "Success"
    Failed = "Failed"

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    order_id = Column(UUID(as_uuid=True), nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, default="INR")
    status = Column(Enum(PaymentStatus), nullable=False)
    gateway_reference = Column(String, nullable=True)
