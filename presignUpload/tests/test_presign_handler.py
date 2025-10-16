from presignUpload.handler import handler

def test_presign_key_format(monkeypatch):
    class MockS3:
        def generate_presigned_url(self, ClientMethod, Params, ExpiresIn):
            assert Params["Key"].startswith("files/")
            return "https://mock-url"

    monkeypatch.setattr("presignUpload.handler.s3", MockS3())
    
    event = {"leadId":"123","fileName":"test.pdf"}
    resp = handler(event, None)
    assert resp["statusCode"] == 200
    body = resp["body"]
    assert body["s3Key"].startswith("files/")
    assert body["traceId"]
    assert body["url"] == "https://mock-url"
