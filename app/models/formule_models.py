from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.orm import relationship
from config.database import Base

class Formule(Base):
    __tablename__ = "formule"
    id_primary = Column('id_primary', Integer, ForeignKey('matter.id'), primary_key=True)
    id_secondary = Column('id_secondary', Integer, ForeignKey('matter.id'), primary_key=True)
    required = Column(Numeric)
    
    matter = relationship("Matter", back_populates="formules", foreign_keys=[id_primary])
    mattert = relationship("Matter", back_populates="formules_sec", foreign_keys=[id_secondary])