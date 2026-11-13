from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: List[Tea] = []

@app.get("/")
def read_root():
    return ("Welcome to the Tea API! Use the endpoints to manage your tea collection.")

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return {"message": "Tea added successfully", "tea": tea}

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for i, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[i] = updated_tea
            return {"message": "Tea updated successfully", "tea": updated_tea}
    return {"message": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for i, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted_tea = teas.pop(i)
            return {"message": "Tea deleted successfully", "tea": deleted_tea}
    return {"message": "Tea not found"}