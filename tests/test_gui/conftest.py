from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from PyQt6.QtWidgets import QApplication


@pytest.fixture(scope="session")
def _qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app


@pytest.fixture
def mock_service():
    svc = MagicMock()
    svc.locale = "en"
    svc._ = lambda key, _locale="en": key
    svc.list_concepts.return_value = []
    svc.get_concept.return_value = None
    svc.search.return_value = []
    svc.explore.return_value = MagicMock(nodes=[], edges=[])
    svc.visualize.return_value = MagicMock(nodes=[], edges=[])
    return svc


@pytest.fixture
def mock_app():
    app = MagicMock()
    return app
