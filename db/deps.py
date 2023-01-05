from typing import Generator
from .session import SessionLocal

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
    finally:
        db.close()