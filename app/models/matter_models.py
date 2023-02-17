from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.orm import relationship
from .formule_models import Formule
# from .history_models import History
from config.database import Base

class Matter(Base):
    __tablename__ = "matter"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="matters")
    # histories = relationship("History", back_populates="matter", foreign_keys=[History.id_matter])
    formules = relationship("Formule", back_populates="matter", foreign_keys=[Formule.id_primary])
    formules_sec = relationship("Formule", back_populates="matter", foreign_keys=[Formule.id_secondary])
