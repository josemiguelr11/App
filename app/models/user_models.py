from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.orm import relationship
from .matter_models import Matter
from ..test.database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user = Column(String, unique=True, index=True)
    password = Column(String, index=True)

    matters = relationship("Matter", back_populates="user")


