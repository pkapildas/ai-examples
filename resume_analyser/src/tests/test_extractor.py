import pytest
from src.resume_parser import PDFExtractor

def test_extract_text_handles_none_input():
    """Assert that passing an invalid file type or None returns an empty string cleanly."""
    result = PDFExtractor.extract_resume_text(None)
    assert result == ""