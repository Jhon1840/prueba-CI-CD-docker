from fastapi import FastAPI

app = FastAPI(title="Python Service")

@app.get("/")

def health():
    variable = int(os.getenv("variable"))
    return {"status": "ok", "variable": variable}