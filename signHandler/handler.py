import boto3
import requests
from datetime import datetime
import uuid

s3 = boto3.client("s3")
BUCKET = "cer-phi-dev"

def handler(event, context):
    # traceId
    trace_id = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4()}"

    # Datos de callback
    deal_id = event.get("dealId")
    brand = event.get("brand")
    download_url = event.get("downloadUrl")
    if not deal_id or not download_url or not brand:
        return {"statusCode":400, "body":"Missing parameters"}

    # Descargar PDF desde URL firmado
    resp = requests.get(download_url)
    if resp.status_code != 200:
        return {"statusCode":500, "body":"Failed to download PDF"}

    yyyy = datetime.utcnow().strftime("%Y")
    mm = datetime.utcnow().strftime("%m")
    s3_key = f"sign/{brand}/{yyyy}/{mm}/{deal_id}/signed.pdf"

    s3.put_object(
        Bucket=BUCKET,
        Key=s3_key,
        Body=resp.content,
        ServerSideEncryption="aws:kms"
    )

    # Log traceId
    print(f"[TRACE] {trace_id} - Saved signed PDF to {s3_key}")

    # Aquí se podría actualizar DynamoDB temporal si aplica
    return {"statusCode":200, "body":{"s3Key": s3_key, "traceId": trace_id}}
