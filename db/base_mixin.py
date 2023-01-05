from sqlalchemy import Column,Integer,DateTime
from pytz import timezone
from datetime import datetime

class BaseMixin:
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone('Asia/Seoul')))
    updated_at = Column(DateTime(timezone=True), nullable=True,onupdate=lambda: datetime.now(timezone('Asia/Seoul')))
    deleted_at = Column(DateTime(timezone=True), nullable=True)