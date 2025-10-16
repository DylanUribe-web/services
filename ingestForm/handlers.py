def healthcheck(event, context):
    return {
        "statusCode": 200,
        "body": '{"status":"ok"}',
        "headers": {"Content-Type": "application/json"}
    }

def form_submit(event, context):
    return {"statusCode": 200, "body": '{"message":"stub"}'}

def file_presign(event, context):
    return {"statusCode": 200, "body": '{"message":"stub"}'}

def file_confirm(event, context):
    return {"statusCode": 200, "body": '{"message":"stub"}'}

def sign_callback(event, context):
    return {"statusCode": 200, "body": '{"message":"stub"}'}
