import boto3
from datetime import datetime, timedelta
import uuid

s3 = boto3.client("s3")
BUCKET = "cer-phi-dev"

def handler(event, context):
    trace_id = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4()}"
    
    lead_id = event.get("leadId")
    file_name = event.get("fileName")
    content_type = event.get("contentType", "application/octet-stream")
    if not lead_id or not file_name:
        return {"statusCode":400, "body":"Missing parameters"}
    
    yyyy = datetime.utcnow().strftime("%Y")
    mm = datetime.utcnow().strftime("%m")
    s3_key = f"files/{lead_id}/{yyyy}/{mm}/{file_name}"
    
    url = s3.generate_presigned_url(
        ClientMethod="put_object",
        Params={"Bucket": BUCKET, "Key": s3_key, "ContentType": content_type, "ServerSideEncryption":"aws:kms"},
        ExpiresIn=600  # 10 min
    )
    
    print(f"[TRACE] {trace_id} - Presign URL {s3_key}")
    
    return {"statusCode":200, "body":{"url":url,"s3Key":s3_key,"traceId":trace_id}}
