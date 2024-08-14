import pytest
from api.config import Config
from .datetime import now

def test_now():
    result = now()
    