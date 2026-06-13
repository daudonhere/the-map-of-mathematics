from __future__ import annotations

from unittest.mock import MagicMock

from PyQt6.QtCore import Qt

from mathverse.core.models import MathConcept
from mathverse.gui.screens.home import HomeScreen


class TestHomeScreen:
    def test_initial_state(self, _qapp, mock_service, mock_app) -> None:
        screen = HomeScreen(mock_service, mock_app)
        assert screen.list_widget.count() == 0

    def test_refresh_populates_list(self, _qapp, mock_service, mock_app) -> None:
        mock_service.list_concepts.return_value = [
            MathConcept(
                id="alg",
                name="Algebra",
                description="...",
                category="Pure",
                locale="en",
            ),
            MathConcept(
                id="geo",
                name="Geometry",
                description="...",
                category="Pure",
                locale="en",
            ),
        ]
        screen = HomeScreen(mock_service, mock_app)
        assert screen.list_widget.count() == 2
        assert "Algebra" in screen.list_widget.item(0).text()

    def test_on_concept_selected(self, _qapp, mock_service, mock_app) -> None:
        mock_service.list_concepts.return_value = [
            MathConcept(
                id="alg",
                name="Algebra",
                description="...",
                category="Pure",
                locale="en",
            ),
        ]
        screen = HomeScreen(mock_service, mock_app)
        screen._on_concept_selected(screen.list_widget.item(0))
        mock_app.show_concept.assert_called_once_with("alg")

    def test_go_back(self, _qapp, mock_service, mock_app) -> None:
        screen = HomeScreen(mock_service, mock_app)
        screen._go_back()
        mock_app.go_splash.assert_called_once()

    def test_key_escape_goes_back(self, _qapp, mock_service, mock_app) -> None:
        screen = HomeScreen(mock_service, mock_app)
        event = MagicMock()
        event.key.return_value = Qt.Key.Key_Escape
        screen.keyPressEvent(event)
        mock_app.go_splash.assert_called_once()
