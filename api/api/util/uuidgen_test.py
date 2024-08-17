import pytest
from .uuidgen import uuidgen
from uuid import UUID

def test_uuidgen():
    result = uuidgen()
    assert type(result) is str
    assert len(result) == 32
    assert result.isalnum() is True
    assert UUID(result)
    