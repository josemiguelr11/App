from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.orm import relationship
from .matter_models import Matter
from .identifier_models import Identifier
from ..test.database import Base

class History(Base):
    __tablename__ = "history"
    date = Column(Date, primary_key=True)
    id_matter = Column(Integer, ForeignKey("matter.id"))
    id_identifier = Column(Integer, primary_key=True)
    value = Column(Integer)

    matter = relationship("Matter", back_populates="histories")
    identifier = relationship("Identifier", back_populates="histories")