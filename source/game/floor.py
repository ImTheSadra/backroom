import pygame as pg
import numpy as np
import math
from .settings import *

class Floor:
    hres = 120
    halfvres = 100

    mod = hres/60
    posx, posy = 0, 0
    objects = []
    def __init__(self, app) -> None:
        self.app = app
        self.window:pg.Surface = app.window
        self.orSurface = pg.image.load("./assest/objects/floor.png")
        self.surface = self.orSurface.copy()

    def update(self):
        self.objects = []
        self.rays = (self.window.get_height()//2)//2
        for ray in range((self.window.get_height()//2)//2):
            self.getObjectsToRender(ray, 2)

    def getObjectsToRender(self, ray:float, offset:int):
        ray += 1
        scale = self.window.get_width()
        width = self.window.get_width()
        height = self.window.get_height()
        delta  = height/self.rays
        print(delta*ray)
        texture = self.surface.subsurface(
            0, height-delta*ray,
            width,
            delta
        )
        pg.image.save(texture, "./t.png")
        pos = (

        )
        self.objects.append([texture, pos])
        

    def draw(self):
        self.window.blit(self.surface, (0,0))