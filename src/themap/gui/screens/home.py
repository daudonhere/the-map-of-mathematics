from __future__ import annotations

from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        label = Label(
            text="Hello, Professor!",
            font_size="48sp",
            halign="center",
            valign="middle",
        )
        self.add_widget(label)
