import boto3
import hashlib
from datetime import datetime
import uuid

s3 = boto3.client("s3")
BUCKET = "cer-phi-dev"

def handler(event, context):
    trace_id = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4()}"

    lead_id = event.get("leadId")
    s3_key = event.get("s3Key")
    sha256 = event.get("sha256")
    size = event.get("size")
    eTag = event.get("eTag")
    if not lead_id or not s3_key:
        return {"statusCode":400, "body":"Missing parameters"}

    # Validar existencia en S3
    try:
        resp = s3.get_object(Bucket=BUCKET, Key=s3_key)
        data = resp["Body"].read()
    except s3.exceptions.NoSuchKey:
        return {"statusCode":404, "body":"File not found"}

    # Validar hash SHA256
    if hashlib.sha256(data).hexdigest() != sha256:
        return {"statusCode":400, "body":"SHA256 mismatch"}

    # Validar tamaño
    if len(data) != size:
        return {"statusCode":400, "body":"Size mismatch"}

    # Publicar evento (simulado aquí con print)
    print(f"[TRACE] {trace_id} - File confirmed: {s3_key}")

    return {"statusCode":200, "body":{"traceId": trace_id}}
