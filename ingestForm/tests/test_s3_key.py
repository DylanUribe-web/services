from ingestForm.s3_key import generate_s3_key

def test_generate_s3_key():
    key = generate_s3_key("dev", "12345", "2025-10-14T10:00:00Z")
    assert key == "forms/dev/2025-10-14/12345/form.json"
