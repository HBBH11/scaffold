# Test-Web-App/main.py
from fastapi import FastAPI

app = FastAPI(title="Test-Web-App")

@app.get("/")
def read_root():
    return {"Hello": "from test-web-app"}