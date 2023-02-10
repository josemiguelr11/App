from sqlalchemy import Column, ForeignKey, Integer, Date, Float
from sqlalchemy.orm import relationship
from config.database import Base

class History(Base):
    __tablename__ = "history"
    date = Column(Date, primary_key=True)
    id_matter = Column(Integer, ForeignKey("matter.id"), primary_key=True)
    id_identifier = Column(Integer, ForeignKey("identifier.id_identifier"), primary_key=True)
    value = Column(Float)

    matter = relationship("Matter", back_populates="histories")
    identifier = relationship("Identifier", back_populates="histories", foreign_keys=[id_identifier])