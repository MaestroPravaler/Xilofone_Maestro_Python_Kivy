# -*- coding: utf-8 -*-

import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from glob import glob
from os.path import dirname, join, basename


##### DEFININDO AS CORES #################################
BLACK = [0, 0, 0, 1]
WHITE = [255, 255, 255, 1]
RED = [255, 0, 0, 1]
ORANGE = [100, 1, 0, 1]
YELLOW = [255, 255, 0, 1]
GREEN = [1, 165, 0, 1]
BLUE = [0, 149, 237, 1]
INDIGO = [0, 0, 139, 1]
VIOLET = [139, 0, 139, 1]
##########################################################

class AudioButton(Button):

    filename = StringProperty(None)
    sound = ObjectProperty(None, allownone=True)
    volume = NumericProperty(1.0)

    def on_press(self):
        if self.sound is None:
            self.sound = SoundLoader.load(self.filename)
        # stop the sound if it's currently playing
        if self.sound.status != 'stop':
            self.sound.stop()
        self.sound.volume = self.volume
        self.sound.play()

    def release_audio(self):
        if self.sound:
            self.sound.stop()
            self.sound.unload()
            self.sound = None

    def set_volume(self, volume):
        self.volume = volume
        if self.sound:
            self.sound.volume = volume


class AudioBackground(BoxLayout):
    pass


class AudioApp(App):

    def build(self):
        nota = 0
        t_y = 0
        root = AudioBackground(spacing=5)
        for fn in glob(join("assets/audio/", '*.wav')):
            nota += 1
            if nota == 1:
                btn = AudioButton(
                    text = 'DÓ',
                    filename = fn,
                    size_hint = (None, None),
                    halign = 'center',
                    size = [80, 380],
                    background_color = RED,
                    text_size=(200, None))
                root.ids.sl.add_widget(btn)

            if nota == 2:
                btn = AudioButton(
                    text="RÉ",
                    filename=fn,
                    size_hint=(None, None),
                    halign='center',
                    size=[80, 370],
                    background_color = ORANGE,
                    text_size=(118, None))
                root.ids.sl.add_widget(btn)

            if nota == 3:
                btn = AudioButton(
                    text="MI",
                    filename=fn,
                    size_hint=(None, None),
                    halign='center',
                    size=[80, 360],
                    background_color = YELLOW,
                    text_size=(118, None))
                root.ids.sl.add_widget(btn)

            if nota == 4:
                btn = AudioButton(
                    text="FÁ",
                    filename=fn,
                    size_hint=(None, None),
                    halign='center',
                    size=[80, 350],
                    background_color = GREEN,
                    text_size=(118, None))
                root.ids.sl.add_widget(btn)

            if nota == 5:
                btn = AudioButton(
                    text="SOL",
                    filename=fn,
                    size_hint=(None, None),
                    halign='center',
                    size=[80, 340],
                    background_color = BLUE,
                    text_size=(118, None))
                root.ids.sl.add_widget(btn)

            if nota == 6:
                btn = AudioButton(
                    text="LÁ",
                    filename=fn,
                    size_hint=(None, None),
                    halign='center',
                    size=[80, 330],
                    background_color = INDIGO,
                    text_size=(118, None))
                root.ids.sl.add_widget(btn)

            if nota == 7:
                btn = AudioButton(
                    text="SÍ",
                    filename=fn,
                    size_hint=(None, None),
                    halign='center',
                    size=[80, 320],
                    background_color = VIOLET,
                    text_size=(118, None))
                root.ids.sl.add_widget(btn)

            if nota == 8:
                btn = AudioButton(
                    text="DÓ",
                    filename=fn,
                    size_hint=(None, None),
                    halign='center',
                    size=[80, 310],
                    background_color = RED,
                    text_size=(118, None))
                root.ids.sl.add_widget(btn)

            if nota == 9:
                btn = AudioButton(
                    text="RÉ",
                    filename=fn,
                    size_hint=(None, None),
                    halign='center',
                    size=[80, 300],
                    background_color = ORANGE,
                    text_size=(118, None))
                root.ids.sl.add_widget(btn)

            if nota == 10:
                btn = AudioButton(
                    text="MI",
                    filename=fn,
                    size_hint=(None, None),
                    halign='center',
                    size=[80, 290],
                    background_color = YELLOW,
                    text_size=(118, None))
                root.ids.sl.add_widget(btn)

            if nota == 11:
                btn = AudioButton(
                    text="FÁ",
                    filename=fn,
                    size_hint=(None, None),
                    halign='center',
                    size=[80, 280],
                    background_color = GREEN,
                    text_size=(118, None))
                root.ids.sl.add_widget(btn)
        return root

    def release_audio(self):
        for audiobutton in self.root.ids.sl.children:
            audiobutton.release_audio()

    def set_volume(self, value):
        for audiobutton in self.root.ids.sl.children:
            audiobutton.set_volume(value)


if __name__ == '__main__':
    AudioApp().run()
