from fastapi import FastAPI, Depends
from app.api.endpoints.users import router as user_router
from app.api.endpoints.tasks import router as task_router
from app.api.endpoints.leaveRequest import router as leave_request_router
from app.api.endpoints.checkIn import router as checkIn_router
from app.api.endpoints.checkOut import router as checkOut_router
from app.api.endpoints.taskAssignment import router as task_assignment_router
from app.api.endpoints.auth import router as auth_router
from app.api.endpoints.abscence import router as abscence_router
from app.api.endpoints.attendance import router as attendance_router
from app.api.endpoints.prediction import router as prediction_router
from sqlalchemy.orm import Session
from app.session import init_db, get_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Application is starting...")
    init_db()  
    yield
    print("Application is shutting down...")

# Initialize FastAPI
app = FastAPI(lifespan=lifespan)
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
app.include_router(leave_request_router, prefix="/leave-requests", tags=["Leave Requests"])
app.include_router(checkIn_router, prefix="/checkIn", tags=["checkIn"])
app.include_router(checkOut_router, prefix="/checkOut", tags=["checkOut"])
app.include_router(task_assignment_router, prefix="/task-assignments", tags=["Task Assignments"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(abscence_router, prefix="/abscence", tags=["Abscence"])
app.include_router(attendance_router, prefix="/attendance", tags=["attendance"])
app.include_router(prediction_router, prefix="/prediction", tags=["prediction"])
