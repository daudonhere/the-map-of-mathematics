from __future__ import annotations

from unittest.mock import MagicMock

from PyQt6.QtCore import Qt

from mathverse.gui.screens.splash_screen import SplashScreen


class TestSplashScreen:
    def test_initial_state(self, _qapp, mock_service, mock_app) -> None:
        screen = SplashScreen(mock_service, mock_app)
        assert screen.title_label.text() == "the_math"
        assert screen.slogan_label.text() == "slogan"
        assert screen.start_btn.text() == "start"
        assert screen.lang_btn.text() == "change_language"

    def test_toggle_language(self, _qapp, mock_service, mock_app) -> None:
        mock_service.locale = "id"
        mock_service.set_locale.side_effect = lambda loc: setattr(
            mock_service, "locale", loc
        )
        screen = SplashScreen(mock_service, mock_app)
        screen._toggle_language()
        assert mock_service.set_locale.called
        assert mock_service.set_locale.call_args[0][0] == "en"

    def test_key_enter_goes_home(self, _qapp, mock_service, mock_app) -> None:
        screen = SplashScreen(mock_service, mock_app)
        event = MagicMock()
        event.key.return_value = Qt.Key.Key_Return
        screen.keyPressEvent(event)
        mock_app.go_home.assert_called_once()

    def test_key_escape_closes(self, _qapp, mock_service, mock_app) -> None:
        screen = SplashScreen(mock_service, mock_app)
        event = MagicMock()
        event.key.return_value = Qt.Key.Key_Escape
        screen.keyPressEvent(event)
        mock_app.close.assert_called_once()
