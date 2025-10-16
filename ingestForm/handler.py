import json
import boto3
from datetime import datetime
import uuid

s3 = boto3.client("s3")
BUCKET = "cer-phi-dev"

def handler(event, context):
    # Generar traceId
    trace_id = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4()}"
    
    # Validar payload mínimo
    form_data = event.get("formData")
    if not form_data or "leadId" not in form_data or "brand" not in form_data:
        return {"statusCode":400, "body":"Invalid payload"}
    
    # Normalizar datos (ejemplo: convertir strings a título)
    form_data["patientName"] = form_data.get("patientName","").title()
    
    lead_id = form_data["leadId"]
    brand = form_data["brand"]
    yyyy = datetime.utcnow().strftime("%Y")
    mm = datetime.utcnow().strftime("%m")
    
    s3_key = f"forms/{brand}/{yyyy}/{mm}/{lead_id}/form.json"
    
    s3.put_object(
        Bucket=BUCKET,
        Key=s3_key,
        Body=json.dumps(form_data),
        ServerSideEncryption="aws:kms"  # usando CMK
    )
    
    print(f"[TRACE] {trace_id} - Saved to {s3_key}")
    
    return {"statusCode":200, "body": json.dumps({"s3Key": s3_key, "traceId": trace_id})}
