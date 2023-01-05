from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.session import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")
    
class Item(Base):
    __tablename__ = "items"

    title = Column(String(100), index=True)
    description = Column(String(100), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")