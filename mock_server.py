from fastapi import FastAPI, Header, Request
import uuid
from datetime import datetime

app = FastAPI()

def log_trace(traceId):
    print(f"[TRACE] {traceId} - {datetime.utcnow().isoformat()}")

@app.post("/form/submit")
async def form_submit(request: Request, x_api_key: str = Header(...), x_hmac_signature: str = Header(...)):
    body = await request.json()
    log_trace(body.get("traceId", str(uuid.uuid4())))
    return {"status": "ok"}

@app.post("/file/presign")
async def file_presign(request: Request, x_api_key: str = Header(...), x_hmac_signature: str = Header(...)):
    body = await request.json()
    log_trace(body.get("traceId", str(uuid.uuid4())))
    return {"url": "https://s3.amazonaws.com/mock-bucket/file.pdf"}

@app.post("/file/confirm")
async def file_confirm(request: Request, x_api_key: str = Header(...), x_hmac_signature: str = Header(...)):
    body = await request.json()
    log_trace(body.get("traceId", str(uuid.uuid4())))
    return {"status": "confirmed"}

@app.post("/sign/callback")
async def sign_callback(request: Request, x_api_key: str = Header(...), x_hmac_signature: str = Header(...)):
    body = await request.json()
    log_trace(body.get("traceId", str(uuid.uuid4())))
    return {"status": "callback received"}
