from __future__ import annotations

from unittest.mock import MagicMock, patch

from PyQt6.QtCore import Qt

from mathverse.core.content import TopicContent
from mathverse.core.models import MathConcept
from mathverse.gui.screens.explore import ExploreScreen


class TestExploreScreen:
    def test_initial_state(self, _qapp, mock_service, mock_app) -> None:
        screen = ExploreScreen(mock_service, mock_app)
        screen.show()
        assert screen.name_label.text() == ""
        assert screen.topics_btn.isVisible() is False

    def test_show_concept_not_found(self, _qapp, mock_service, mock_app) -> None:
        mock_service.get_concept.return_value = None
        screen = ExploreScreen(mock_service, mock_app)
        screen.show_concept("unknown")
        assert screen.name_label.text() == "concept_not_found"

    def test_show_concept_found(self, _qapp, mock_service, mock_app) -> None:
        concept = MathConcept(
            id="alg",
            name="Algebra",
            description="Study of symbols",
            category="Pure Mathematics",
            related_concepts=["geometry"],
        )
        mock_service.get_concept.return_value = concept
        with patch("mathverse.gui.screens.explore.get_content", return_value=None):
            screen = ExploreScreen(mock_service, mock_app)
            screen.show_concept("alg")
            assert screen.name_label.text() == "Algebra"
            assert "Pure" in screen.category_label.text()

    def test_show_concept_with_topics(self, _qapp, mock_service, mock_app) -> None:
        concept = MathConcept(
            id="alg",
            name="Algebra",
            description="...",
            category="Math",
            related_concepts=[],
        )
        mock_service.get_concept.return_value = concept
        content = TopicContent(concept_id="alg", subtopics=[MagicMock()])
        with patch(
            "mathverse.gui.screens.explore.get_content", return_value=content
        ):
            screen = ExploreScreen(mock_service, mock_app)
            screen.show()
            screen.show_concept("alg")
            assert screen.topics_btn.isVisible() is True

    def test_show_concept_no_topics(self, _qapp, mock_service, mock_app) -> None:
        concept = MathConcept(
            id="geo",
            name="Geometry",
            description="...",
            category="Math",
            related_concepts=[],
        )
        mock_service.get_concept.return_value = concept
        with patch("mathverse.gui.screens.explore.get_content", return_value=None):
            screen = ExploreScreen(mock_service, mock_app)
            screen.show()
            screen.show_concept("geo")
            assert screen.topics_btn.isVisible() is False

    def test_key_escape_goes_home(self, _qapp, mock_service, mock_app) -> None:
        screen = ExploreScreen(mock_service, mock_app)
        event = MagicMock()
        event.key.return_value = Qt.Key.Key_Escape
        screen.keyPressEvent(event)
        mock_app.go_home.assert_called_once()
