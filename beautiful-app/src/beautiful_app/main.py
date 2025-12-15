# Beautiful-App/main.py
from fastapi import FastAPI

app = FastAPI(title="Beautiful-App")

@app.get("/")
def read_root():
    return {"Hello": "from beautiful-app"}