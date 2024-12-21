from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL
DATABASE_URL = "postgresql://postgres:helloworld123@localhost:5432/postgres"

# Create an engine
engine = create_engine(DATABASE_URL)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_database_connection():
    try:
        # Create a session
        session = SessionLocal()

        # Attempt a simple query
        result = session.execute("SELECT 1")
        print("Database connection successful!")
        session.close()
    except Exception as e:
        print(f"Error connecting to the database: {e}")

if __name__ == "__main__":
    test_database_connection()
