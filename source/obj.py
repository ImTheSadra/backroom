import pygame as pg
import math
from .settings import *

class ObjectRenderer:
    def __init__(self, runner) -> None:
        self.runner = runner
        self.window:pg.Surface = runner.window
        self.wallTextures = self.loadWallTextures()
        self.sky = self.getTexture("./assest/sky.png")
        self.sky.fill((250,206,98))
        self.skyOffset = 0
    
    def draw(self):
        self.drawBackground()
        self.renderGameObject()

    def drawBackground(self):
        self.skyOffset = (
            self.skyOffset + 4.5 * self.runner.player.rel
        ) % self.window.get_width()
        self.window.blit(self.sky, (-self.skyOffset, 0))
        self.window.blit(
            self.sky, 
            (
                -self.skyOffset + self.window.get_width(),
                0
            )
        )
        pg.draw.rect(
            self.window,
            (250,206,98),
            (
                0, self.window.get_height() / 2,
                self.window.get_width(),
                self.window.get_height()
            )
        )
    
    def renderGameObject(self):
        objects = sorted(
            self.runner.rayCasting.objectsToRender,
            key=lambda t: t[0], reverse=True
        )
        for dpeth, image, pos in objects:
            self.window.blit(
                image, pos
            )
    
    @staticmethod
    def getTexture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        result = pg.image.load(path).convert_alpha()
        return result
    
    def loadWallTextures(self):
        return {
            1: self.getTexture("./assest/objects/1.png"),
            2: self.getTexture("./assest/objects/2.png"),
            3: self.getTexture("./assest/objects/3.png")
        }