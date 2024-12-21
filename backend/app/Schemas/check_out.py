from datetime import date, time

class CheckOutCreate(BaseModel):
    employee_id: int  # Foreign key to `User.id`
    check_in_id: int  # Foreign key to `CheckIn.id`
    date: date
    time: time