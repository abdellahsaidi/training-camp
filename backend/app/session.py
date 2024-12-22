import pkgutil
import importlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

# Replace with your actual database credentials
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:helloworld123@localhost:5432/postgres"

# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"options": "-c timezone=utc"})

# Create a sessionmaker to manage connections
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the models
Base = declarative_base()

# Dependency function for FastAPI routes
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Automatically create all tables (useful for development)
def init_db():
    import app.db.models  # Ensure the `models` module is imported
    package_path = app.db.models.__path__
    for _, module_name, _ in pkgutil.iter_modules(package_path):
        importlib.import_module(f"app.db.models.{module_name}")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")
