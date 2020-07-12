import pygame


class Level:
    def __init__(self):
        pass

    def draw(self):
        pass


class Start_Level(Level):
    def __init__(self, window):
        self.window = window

    def draw(self):
        self.window.fill((19, 156, 71))
