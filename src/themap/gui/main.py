from __future__ import annotations

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from themap.gui.screens.explore import ExploreScreen
from themap.gui.screens.home import HomeScreen
from themap.gui.screens.visualize import VisualizeScreen
from themap.utils.config import Config


class TheMapApp(App):
    def build(self) -> ScreenManager:
        Window.size = (Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)
        Window.minimum_width = Config.WINDOW_MIN_WIDTH
        Window.minimum_height = Config.WINDOW_MIN_HEIGHT

        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ExploreScreen(name="explore"))
        sm.add_widget(VisualizeScreen(name="visualize"))
        return sm


def main() -> None:
    TheMapApp().run()
