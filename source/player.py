from .settings import *
import pygame as pg
import math
from pygame.constants import *
from .map import MiniMap
import numpy as np

class Player:
    rel = 0
    speed = 0.06
    def __init__(self, runner) -> None:
        self.runner = runner
        self.window:pg.Surface = runner.window
        self.map:MiniMap = runner.map
        self.x, self.y = 2, 2
        self.angle = 0
    
    def movement(self):
        sinA = math.sin(self.angle)
        cosA = math.cos(self.angle)

        dx, dy = 0, 0

        speedSin = self.speed * sinA
        speedCos = self.speed * cosA

        vSpeedSin = self.speed * math.sin(self.angle+1.5707963267948966)
        vSpeedCos = self.speed * math.cos(self.angle+1.5707963267948966)

        keys = pg.key.get_pressed()
        if keys[K_w]:
            dx += speedCos
            dy += speedSin
        if keys[K_s]:
            dx -= speedCos
            dy -= speedSin
        if keys[K_d]:
            dx += vSpeedCos
            dy += vSpeedSin
        if keys[K_a]:
            dx -= vSpeedCos
            dy -= vSpeedSin
        
        self.checkWallCollition(dx, dy)

        if keys[K_LEFT]:
            self.angle -= 0.03
        if keys[K_RIGHT]:
            self.angle += 0.03
    
    def checkWall(self, x:int, y:int):
        return not self.map.miniMap[y][x] != 0
    
    def checkWallCollition(self, x, y):
        if self.checkWall(int(self.x + x), int(self.y)):
            self.x += x
        if self.checkWall(int(self.x), int(self.y + y)):
            self.y += y
    
    def draw(self):
        pg.draw.circle(
            self.window,
            (200, 0, 200),
            (self.x * 100, self.y * 100),
            15
        )

        cos, sin = math.cos(self.angle), math.sin(self.angle)
        pg.draw.line(
            self.window,
            (200, 0, 200),
            (
                self.x * 100 + (cos*50),
                self.y * 100 + (sin*50)
            ), (
                self.x * 100,
                self.y * 100
            )
        )

    def mouseContorol(self):
        x, y = pg.mouse.get_pos()
        if x < MOUSE_BORDER_LEFT or x > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos(
                (
                    self.window.get_width()/2,
                    self.window.get_height()/2
                )
            )
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSIITY

    def update(self):
        self.movement()
    
    @property
    def pos(self):
        return self.x, self.y

    @property
    def mapPos(self):
        return int(self.x), int(self.y)
