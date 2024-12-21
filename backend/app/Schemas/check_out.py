from datetime import date, time

class CheckOutCreate(BaseModel):
    employee_id: int  
    check_in_id: int  
    date: date
    time: time