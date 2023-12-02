import pygame as pg
from .settings import *
from .player import Player
from PIL import Image
from .settings import *

class SpriteObject:
    frames = []
    frame = 0
    path = "./assest/sprite/1.png"
    def __init__(self, runner, path:str=None, pos=(9.5,3.5)) -> None:
        self.runner = runner
        self.player:Player = runner.player
        self.x, self.y = pos
        try:img = Image.open(path)
        except:img = Image.open(self.path)
        for i in range(img.n_frames):
            img.seek(i)
            rgba = img.convert("RGBA")
            surf = pg.image.fromstring(
                rgba.tobytes(),
                rgba.size,
                "RGBA"
            )
            # surf = pg.transform.scale(
            #     surf,
            #     (
            #         surf.get_width()*3,
            #         surf.get_height()*3
            #     )
            # )
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

class Enemy(SpriteObject):
    target = None
    def checkWall(self, x:int, y:int):
        return not self.runner.map.miniMap[y][x] > 0
    
    def checkWallCollition(self, x, y):
        if self.checkWall(int(self.x + x), int(self.y)):
            self.x += x
        if self.checkWall(int(self.x), int(self.y + y)):
            self.y += y

    def getTarget(self):
        x = []
        for value in range(140, 160):
            x.append(value/100)
        y = []

        for value in range(140, 160):
            y.append(value/100)
        return x, y

    def update(self):
        # if self.target == None:self.target = self.getTarget()
        # dx, dy = 0, 0
        # tx, ty = self.target

        # if not self.x in tx:
        #     if self.x > 1.5:
        #         dx -= 0.02
        #     elif self.x < 1.5:
        #         dx += 0.02

        # if not self.y in ty:
        #     if self.y > 1.5:
        #         dy -= 0.02
        #     elif self.y < 1.5:
        #         dy += 0.02

        # if dx != 0 or dy != 0:
        #     self.frame += 0.1
        #     if round(self.frame) >= len(self.frames):
        #         self.frame = 0
        # else:
        #     self.frame = 0

        # self.checkWallCollition(dx, dy)

        return super().update()
