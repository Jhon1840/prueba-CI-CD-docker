from fastapi import FastAPI

app = FastAPI(title="Python Service")

@app.get("/")

def health():
    
    return {"status": "ok"}