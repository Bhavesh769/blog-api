from fastapi import FastAPI
from app.database import engine

app = FastAPI()

@app.get("/")
def test_connection():
    try:
        conn = engine.connect()
        conn.close()
        return {"message": "Database connection successful"}
    except Exception as e:
        return {"message": f"Database connection failed: {str(e)}"}
  