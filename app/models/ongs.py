from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils import generate_uuid


class Ong(Base):
    __tablename__ = "ongs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String(36), nullable=False, unique=True, default=lambda: generate_uuid())
    name = Column(String, nullable=False, unique=True) # Nome Fantasia
    business_name = Column(String, nullable=False, unique=True) # Razão Social
    state_registration = Column(String, nullable=False, unique=True) # Inscrição Estadual
    phone_number = Column(String(11), nullable=False, unique=True)
    cnpj = Column(String(14), nullable=False, unique=True)
    id_address = Column(Integer, ForeignKey("addresses.id"), nullable=False)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())

    address = relationship("Address", backref="ong", uselist=False)

    def __repr__(self) -> str:
        return "<Ong %s>" % self.id