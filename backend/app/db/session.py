from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import models

# Create all tables if they don't exist
Base.metadata.create_all(bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
