import pygame as pg
import sys
from .font import Font, init
init()

from .home import Home
from .game import Game
from .about import Info

class App:
    running = False
    apps = {}
    def __init__(self) -> None:
        self.init = pg.init()
        self.window = pg.display.set_mode((1200, 700), pg.RESIZABLE)
        pg.display.set_caption("اتاق پشتی")
        self.clock = pg.time.Clock()
        self.font = Font("./assest/font/fa.ttf", 30)
        self.apps["home"] = Home(self)
        self.apps["home"].running = True
        self.apps["game"] = Game(self)
        self.apps["info"] = Info(self)

    def loop(self):
        self.window.fill((30,10,10))

        for app in self.apps:
            self.apps[app].loop()

        self.fps = self.clock.get_fps()
        self.clock.tick(60)

        txt = self.font.render(
            "fps : "+str(self.fps)[:4], (200, 50, 200)
        )
        self.window.blit(
            txt, (5, 5)
        )

        pg.display.flip()
        pg.display.update()

    def run(self):
        self.running = True

        while self.running:
            self.loop()

        pg.quit()
        sys.exit()