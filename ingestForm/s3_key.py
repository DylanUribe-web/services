from datetime import datetime

def generate_s3_key(environment: str, form_id: str, submitted_at_iso: str = None) -> str:
    if submitted_at_iso:
        try:
            dt = datetime.fromisoformat(submitted_at_iso.replace("Z", "+00:00"))
        except Exception:
            dt = datetime.utcnow()
    else:
        dt = datetime.utcnow()
    date_part = dt.date().isoformat()
    return f"forms/{environment}/{date_part}/{form_id}/form.json"
