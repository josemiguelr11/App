from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.orm import relationship

from ..test.database import Base

class Identifier(Base):
    __tablename__ = "identifier"
    id_identifier = Column(Integer, primary_key=True)
    name = Column(String(length=1))

    histories = relationship("History", back_populates="identifier")