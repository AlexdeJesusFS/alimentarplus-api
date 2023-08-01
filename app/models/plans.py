from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils import generate_uuid


class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String(36), nullable=False, unique=True, default=lambda: generate_uuid())
    name = Column(String, nullable=False, unique=True)
    price = Column(String, nullable=False)
    description = Column(String)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())

    supermarkets = relationship("Supermarket", backref="plan")

    def __repr__(self) -> str:
        return "<Plan %s>" % self.id