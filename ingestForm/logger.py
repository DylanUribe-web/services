import logging
import sys
from pythonjsonlogger import jsonlogger

def get_logger(lambda_name: str, environment: str, trace_id: str):
    logger = logging.getLogger(lambda_name)
    logger.setLevel(logging.INFO)
    logHandler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter('%(traceId)s %(timestamp)s %(level)s %(message)s %(extra)s')
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger = logging.LoggerAdapter(logger, {
        "traceId": trace_id,
        "timestamp": "2025-10-14T11:00:00Z",  # o datetime.utcnow().isoformat()
        "extra": {"lambdaName": lambda_name, "environment": environment}
    })
    return logger
