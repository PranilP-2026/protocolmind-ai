from fastapi import FastAPI

app = FastAPI(title="ProtocolMind AI")


@app.get("/")
async def root():
    return {"message": "ProtocolMind AI Backend"}
