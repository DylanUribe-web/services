from ingestForm.handler import handler

def test_ingestform_key_format(monkeypatch):
    # mock S3 put_object
    class MockS3:
        def put_object(self, Bucket, Key, Body, ServerSideEncryption):
            assert Key.startswith("forms/")
            return True

    monkeypatch.setattr("ingestForm.handler.s3", MockS3())

    event = {"formData":{"leadId":"123","brand":"cer","patientName":"juan"}}
    resp = handler(event, None)
    assert resp["statusCode"] == 200
    assert "s3Key" in resp["body"]
    assert "traceId" in resp["body"]
