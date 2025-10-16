import hashlib
from signHandler.handler import handler

def test_sign_handler_full(monkeypatch):
    # 1️⃣ Mock S3
    class MockS3:
        def put_object(self, Bucket, Key, Body, ServerSideEncryption):
            # Verificar que el archivo se sube al path correcto
            assert Key.startswith("sign/")
            # Verificar tamaño del archivo
            assert len(Body) == len(b"PDF content")
            # Verificar SHA256 del contenido
            sha256 = hashlib.sha256(Body).hexdigest()
            expected_sha256 = hashlib.sha256(b"PDF content").hexdigest()
            assert sha256 == expected_sha256
            print(f"[TEST] SHA256: {sha256}, size: {len(Body)} bytes")
            return True

    monkeypatch.setattr("signHandler.handler.s3", MockS3())

    # 2️⃣ Mock requests.get
    class MockResp:
        status_code = 200
        content = b"PDF content"

    monkeypatch.setattr(
        "signHandler.handler.requests",
        type("MockRequests", (), {"get": lambda url: MockResp()})
    )

    # 3️⃣ Llamar handler con evento simulado
    event = {"dealId":"123","brand":"cer","downloadUrl":"https://mock-url"}
    resp = handler(event, None)

    # 4️⃣ Verificaciones finales
    body = resp["body"]
    assert resp["statusCode"] == 200
    assert "s3Key" in body
    assert "traceId" in body
