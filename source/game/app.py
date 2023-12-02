import sys
import pygame as pg
from pygame.constants import *
from .player import Player
from .map import MiniMap
from .obj import ObjectRenderer
from .raycasting import RayCasting
from .spr import SpriteObject, Enemy
from .lamp import Lamp
from .floor import Floor

class Game:
    running = False
    def __init__(self, app) -> None:
        pg.init()
        pg.font.init()
        self.window = app.window
        self.newGame()
        self.app = app
    
    def newGame(self):
        self.map = MiniMap(self)
        self.player = Player(self)
        self.objectRenderer = ObjectRenderer(self)
        self.rayCasting = RayCasting(self)
        self.staticSprite = Enemy(self)
        self.lamp = Lamp(self, "./assest/sprite/lamp.gif", (1.5,1.5))
        self.floor = Floor(self)

    def update(self):
        self.player.update()
        self.rayCasting.update()
        self.staticSprite.update()
        self.lamp.update()

    def draw(self):
        self.window.fill((250,206,95))
        self.objectRenderer.draw()

    def checkEvent(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.app.running = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                    self.app.running = False
    
    def loop(self):
        if not self.running:
            return
        self.update()
        self.draw()
        self.checkEvent()