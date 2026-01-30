import sys
from pathlib import Path
import pytest
from unittest.mock import MagicMock

# Add src/ to PYTHONPATH before test collection
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


@pytest.fixture
def db_session():
    return MagicMock()
