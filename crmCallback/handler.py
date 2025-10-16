from crmCallback.logger import get_logger
import uuid
from datetime import datetime, timezone

def handler(event, context):
    trace_id = f"{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}-{uuid.uuid4()}"
    logger = get_logger("crmCallback", "dev", trace_id)
    logger.info("Lambda invoked", extra={"event": event})
    return {"statusCode": 200, "body": '{"message":"ok"}'}
