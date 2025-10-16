from signHandler.handler import handler

def test_sign_handler(monkeypatch):
    # Mock S3 put_object y requests.get
    class MockS3:
        def put_object(self, Bucket, Key, Body, ServerSideEncryption):
            assert Key.startswith("sign/")
            return True
    monkeypatch.setattr("signHandler.handler.s3", MockS3())

    class MockResp:
        status_code = 200
        content = b"PDF content"
    monkeypatch.setattr("signHandler.handler.requests", type('MockRequests', (), {"get": lambda url: MockResp()}))

    event = {"dealId":"123","brand":"cer","downloadUrl":"https://mock-url"}
    resp = handler(event, None)
    assert resp["statusCode"] == 200
    body = resp["body"]
    assert "s3Key" in body
    assert "traceId" in body
