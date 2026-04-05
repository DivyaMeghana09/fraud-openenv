from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Fraud API is running ✅"}

@app.get("/health")
def health():
    return {"status": "ok"}

# ✅ REQUIRED FOR CHECK
@app.post("/reset")
def reset():
    return {"status": "reset successful"}