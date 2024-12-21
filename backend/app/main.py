from fastapi import FastAPI
from app.database import Base, engine


# Initialize DB
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI()

# Include Routers
app.include_router(test_connection.router, prefix="/test", tags=["test"])