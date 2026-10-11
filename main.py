from fastapi import FastAPI,HTTPException

app = FastAPI()

expenses={
    1:{"description":"book","amount":66.7},
    2:{"description": "gym", "amount": 90.5},
    3:{"description":"food","amount":500},
    4:{"description":"univercity","amount":9000}
    }


@app.get("/expenses")
def show_all():
    return expenses

@app.get("/expenses/{expense_id}")
def show_id(expense_id:int):
    if expense_id in expenses :
        return expenses[expense_id]
    raise HTTPException (status_code=404,detail="not found")

@app.post("/expenses",status_code=201)
def expenses_create(description:str,amount:float):
    new_id=max(expenses.keys(),default=0)+1
    expenses[new_id]={"description":description,"amount":amount}
    return {"id":new_id,"description":description,"amount":amount}

@app.put("/expenses/{expense_id}")
def expenses_update(expense_id:int,description:str,amount:float):
    if expense_id in expenses:
        expenses[expense_id]={"description":description,"amount":amount}
        return {"id":expense_id,"description":description,"amount":amount}
    raise HTTPException(404,"not_found")

@app.delete("/expenses/{expense_id}")
def expenses_delete(expense_id:int):
    if expense_id in expenses:
        
        return expenses.pop(expense_id)
    raise HTTPException(404,"not_found")