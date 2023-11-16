import sys
import pygame as pg
from pygame.constants import *
from .player import Player
from .map import MiniMap
from .obj import ObjectRenderer
from .raycasting import RayCasting

class Runner:
    running = False
    def __init__(self) -> None:
        pg.init()
        self.window = pg.display.set_mode((1200, 700))
        self.clock = pg.time.Clock()
        pg.display.set_caption("اتاق پشتی")
        self.newGame()
    
    def newGame(self):
        self.map = MiniMap(self)
        self.player = Player(self)
        self.objectRenderer = ObjectRenderer(self)
        self.rayCasting = RayCasting(self)

    def update(self):
        self.player.update()
        self.rayCasting.update()

        pg.display.flip()
        pg.display.update()
        self.clock.tick(60)
    
    def draw(self):
        self.window.fill((51,51,51))
        self.objectRenderer.draw()

    def checkEvent(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
    
    def gameLoop(self):
        self.draw()
        self.checkEvent()
        self.update()

    def run(self):
        self.running = True

        while self.running:
            self.gameLoop()
        
        pg.quit()
        sys.exit()