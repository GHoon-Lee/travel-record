from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import DB_URL
from .base_mixin import BaseMixin


engine = create_engine(
    DB_URL,
    pool_recycle=500,
    echo=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



Base = declarative_base(cls=BaseMixin)