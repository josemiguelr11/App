from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.orm import relationship
from ..test.database import Base

class Formule(Base):
    __tablename__ = "formule"
    id_primary = Column(Integer, primary_key=True)
    id_secundary = Column(Integer)
    required = Column(Numeric)
    
    matter = relationship("Matter", back_populates="formules")
    mattert = relationship("Matter", back_populates="formules_sec")