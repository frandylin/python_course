from fastapi import FastAPI

app = FastAPI() #FastAPI 物件
@app.get("/")
def index():
    return "Hi Frandy!"