from fastapi import FastAPI

app = FastAPI(
    title="StreamForge",
    version="0.1.0",
    description="DeepStream pipeline host with FastAPI control plane",
)

@app.get("/status")
def status():
    return {"status": "RUNNING"}

@app.get("/metrics")
def metrics():
    return {"active_streams": 0, "streams": {}}