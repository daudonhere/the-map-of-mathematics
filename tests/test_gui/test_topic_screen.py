from __future__ import annotations

from unittest.mock import MagicMock, patch

from PyQt6.QtCore import Qt

from mathverse.core.content import SubTopic, TopicContent
from mathverse.gui.screens.topic import TopicScreen


def _make_subtopic(
    title_en: str = "Test",
    desc_en: str = "A test subtopic",
    explanation_en: str = "Explanation",
    examples_en: list[str] | None = None,
    playground: str | None = None,
) -> SubTopic:
    return SubTopic(
        title={"en": title_en, "id": title_en},
        description={"en": desc_en, "id": desc_en},
        explanation={"en": explanation_en, "id": explanation_en},
        examples={
            "en": examples_en or ["Example 1", "Example 2"],
            "id": examples_en or ["Example 1", "Example 2"],
        },
        playground=playground,
    )


class TestTopicScreen:
    def test_initial_state(self, _qapp, mock_service, mock_app) -> None:
        screen = TopicScreen(mock_service, mock_app)
        assert screen.subtopic_list.count() == 0

    def test_show_topic_not_found(self, _qapp, mock_service, mock_app) -> None:
        screen = TopicScreen(mock_service, mock_app)
        screen.show_topic("unknown")
        assert screen.concept_label.text() == "concept_not_found"

    def test_show_topic_found(self, _qapp, mock_service, mock_app) -> None:
        subtopics = [
            _make_subtopic("Variables", "About variables"),
            _make_subtopic("Operations", "About operations"),
        ]
        content = TopicContent(concept_id="algebra", subtopics=subtopics)
        with patch(
            "mathverse.gui.screens.topic.get_content", return_value=content
        ):
            screen = TopicScreen(mock_service, mock_app)
            screen.show_topic("algebra")
            assert screen.subtopic_list.count() == 2
            assert "Variables" in screen.subtopic_list.item(0).text()

    def test_detail_view_renders(
        self, _qapp, mock_service, mock_app
    ) -> None:
        subtopic = _make_subtopic(
            "Factoring",
            "Learn factoring",
            "First factor\nThen simplify",
            ["x^2 + 2x = x(x+2)", "x^2 - 4 = (x-2)(x+2)"],
            playground="factoring",
        )
        content = TopicContent(
            concept_id="algebra", subtopics=[subtopic]
        )
        with patch(
            "mathverse.gui.screens.topic.get_content", return_value=content
        ):
            screen = TopicScreen(mock_service, mock_app)
            screen.show()
            screen.show_topic("algebra")
            screen._on_subtopic_activated(screen.subtopic_list.item(0))
            assert screen._current_detail_subtopic is not None
            assert (
                screen.detail_title.text()
                == subtopic.title.get("en")
            )
            assert screen.playground_btn.isVisible() is True

    def test_detail_no_playground(
        self, _qapp, mock_service, mock_app
    ) -> None:
        subtopic = _make_subtopic(
            "Theory", "Just theory", "Some explanation"
        )
        content = TopicContent(
            concept_id="algebra", subtopics=[subtopic]
        )
        with patch(
            "mathverse.gui.screens.topic.get_content", return_value=content
        ):
            screen = TopicScreen(mock_service, mock_app)
            screen.show()
            screen.show_topic("algebra")
            screen._on_subtopic_activated(screen.subtopic_list.item(0))
            assert screen.playground_btn.isVisible() is False

    def test_key_tab_goes_back_to_list(
        self, _qapp, mock_service, mock_app
    ) -> None:
        subtopics = [_make_subtopic("Test", "Desc", "Expl")]
        content = TopicContent(concept_id="alg", subtopics=subtopics)
        with patch(
            "mathverse.gui.screens.topic.get_content", return_value=content
        ):
            screen = TopicScreen(mock_service, mock_app)
            screen.show()
            screen.show_topic("alg")
            screen._on_subtopic_activated(screen.subtopic_list.item(0))
            assert screen.stack.currentIndex() == 1

            event = MagicMock()
            event.key.return_value = Qt.Key.Key_Tab
            screen.keyPressEvent(event)
            assert screen.stack.currentIndex() == 0

    def test_key_escape_goes_back(
        self, _qapp, mock_service, mock_app
    ) -> None:
        screen = TopicScreen(mock_service, mock_app)
        event = MagicMock()
        event.key.return_value = Qt.Key.Key_Escape
        screen.keyPressEvent(event)
        mock_app.go_home.assert_called_once()
