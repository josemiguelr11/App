from sqlalchemy import Boolean, Column, Integer, Sequence, String
from sqlalchemy.orm import relationship
from config.database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user = Column(String, unique=True, index=True)
    password = Column(String, index=True)

    matters = relationship("Matter", back_populates="user")


