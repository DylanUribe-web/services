from fileConfirm.handler import handler
import hashlib

def test_file_confirm(monkeypatch):
    class MockS3Body:
        def read(self): return b"testdata"
    class MockS3:
        class exceptions:
            class NoSuchKey(Exception): pass
        def get_object(self, Bucket, Key):
            return {"Body": MockS3Body()}
    monkeypatch.setattr("fileConfirm.handler.s3", MockS3())

    data = b"testdata"
    sha = hashlib.sha256(data).hexdigest()
    event = {"leadId":"123","s3Key":"dummy","size":len(data),"sha256":sha,"eTag":"mock"}
    resp = handler(event, None)
    assert resp["statusCode"] == 200
    assert "traceId" in resp["body"]
