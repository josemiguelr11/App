from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base

class Identifier(Base):
    __tablename__ = "identifier"
    id_identifier = Column(Integer, primary_key=True)
    name = Column(String)

    histories = relationship("History", back_populates="identifier")