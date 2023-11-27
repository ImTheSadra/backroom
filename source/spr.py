import pygame as pg
from .settings import *
from .player import Player
from PIL import Image

class SpriteObject:
    frames:list[pg.Surface] = []
    frame = 0
    path = "./assest/player.git"
    def __init__(self, runner, path:str=None, pos=(9.5,3.5)) -> None:
        self.runner = runner
        if path == None:path = self.path
        self.player:Player = runner.player
        self.x, self.y = pos
        img = Image.open("./assest/sprite/2.gif")
        for i in range(img.n_frames):
            img.seek(i)
            rgba = img.convert("RGBA")
            surf = pg.image.fromstring(
                rgba.tobytes(),
                rgba.size,
                "RGBA"
            )
            surf = pg.transform.scale(
                surf,
                (
                    surf.get_width()*3,
                    surf.get_height()*3
                )
            )
            self.frames.append(surf)
        self.width = self.frames[0].get_width()
        self.halfWidth = self.frames[0].get_width() // 2
        self.window:pg.Surface = runner.window
        self.ratio = self.width / self.frames[0].get_height()
        self.dx, self.dy, self.theta, self.screenX, self.dist, self.normDist = (
            0, 0, 0, 0, 1, 1
        )
        self.spriteHalfWidth = 0

    def getSpriteProjection(self):
        proj = SCREEN_DIST / self.normDist
        projWidth, projHeight = proj * self.ratio, proj

        image = pg.transform.scale(self.frames[round(self.frame)], (projWidth, projHeight))

        self.spriteHalfWidth = projWidth // 2
        pos = (
            self.screenX - self.spriteHalfWidth, 
            self.window.get_height() // 2 - projHeight // 2
        )

        self.runner.rayCasting.objectsToRender.append(
            (self.normDist, image, pos)
        )

    def getSprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle

        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau
        
        deltaRays = delta / DELTA_ANGLE
        self.screenX = (
            ((self.window.get_width()//2)//2) + deltaRays
        ) * SCALE 

        self.dist = math.hypot(dx, dy)
        self.normDist = self.dist * math.cos(delta)
        if -self.halfWidth < self.screenX < (self.window.get_width() + self.halfWidth) and self.normDist > 0.5:
            self.getSpriteProjection()


    def update(self):
        self.getSprite()
        self.frame += 0.1
        if round(self.frame) >= len(self.frames):
            self.frame = 0

class Enemy(SpriteObject):
    def update(self):
        if self.x > self.player.x:
            self.x -= 0.01
        if self.x < self.player.x:
            self.x += 0.01
        if self.y > self.player.y:
            self.y -= 0.01
        if self.y < self.player.y:
            self.y += 0.01
        return super().update()