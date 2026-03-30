from fastapi import FastAPI
from server.environment import FraudEnv

app = FastAPI()
env = FraudEnv()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: int):
    return env.step(action)