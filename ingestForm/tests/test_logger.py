from ingestForm.logger import get_logger

def test_logger_format(capsys):
    logger = get_logger("ingestForm", "dev", "trace123")
    logger.info("Test message")
    captured = capsys.readouterr()
    assert "trace123" in captured.out
    assert "Test message" in captured.out
