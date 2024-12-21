from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace the credentials in the connection string
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:helloworld123@localhost:5432/postgres"

# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"options": "-c timezone=utc"})

# Create a sessionmaker to manage connections
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the models
Base = declarative_base()
