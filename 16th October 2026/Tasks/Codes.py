
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class Employee(BaseModel):
    id: int
    name: str
    department: str
    designation: str
    salary:float
    city: str

employees=[]
@app.get("/docs")
def read_docs():
    return "Employee Management System"
@app.post("/employees")
def create_employees(employee: Employee):
    employees.append(employee)
    return{
        'message': 'Employee added',
        'employee':employee
    }

@app.get("/employees")
def read_employees():
    return employees

@app.get("/employees/{employee_id}")
def read_employee(employee_id: int):
    for employee in employees:
        if employee.id == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):
    for index, employee in enumerate(employees):
        if employee.id == employee_id:
            employees[index] = updated_employee
            return employee
    raise HTTPException(status_code=404,detail="Employee not found")

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for employee in employees:
        if employee.id == employee_id:
            employees.remove(employee)
            return "Employee deleted"
    raise HTTPException(status_code=404,detail="Employee not found")

