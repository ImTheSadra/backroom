import pygame as pg
import math
from .settings import *
from .map import MiniMap

class RayCasting:
    rayCastingResult = []
    objectsToRender = []
    def __init__(self, runner) -> None:
        self.runner = runner
        self.map:MiniMap = runner.map
        self.window:pg.Surface = runner.window
        self.textures = runner.objectRenderer.wallTextures

    def getObjectToRender(self):
        self.objectsToRender = []
        for ray, value in enumerate(self.rayCastingResult):
            depth, projHeight, texture, offset = value
            texture:pg.Surface = self.textures[texture]
            numRays = self.window.get_width()//2
            scale = self.window.get_width() // numRays

            if projHeight < self.window.get_height():
                wallColumn = texture.subsurface(
                    offset * (TEXTURE_SIZE - scale ),
                    0, SCALE, TEXTURE_SIZE
                )
                wallColumn = pg.transform.scale(wallColumn, (scale, projHeight))
                wallPos = (ray * scale, (self.window.get_height() // 2) - projHeight // 2)
            else:
                textureHeight = TEXTURE_SIZE * self.window.get_height() / projHeight
                
                wallColumn = texture.subsurface(
                    offset * (TEXTURE_SIZE - scale), 
                    HALF_TEXTURE_SIZE - (textureHeight // 2),
                    scale, textureHeight
                )
                wallColumn = pg.transform.scale(
                    wallColumn, (scale, self.window.get_height())
                )
                wallPos = (ray * scale, 0)

            self.objectsToRender.append(
                (depth, wallColumn, wallPos)
            )

    def rayCast(self):
        self.rayCastingResult = []
        ox, oy = self.runner.player.pos
        xMap, yMap = self.runner.player.mapPos

        xHor, yHor = 1, 1

        angleA = self.runner.player.angle - HALF_FOV + 0.0001
        

        for ray in range(self.window.get_width()//2):
            
            sinA = math.sin(angleA)
            cosA = math.cos(angleA)
            # math
            # hori

            yHor, dy = (yMap + 1, 1) if sinA > 0 else (yMap - 1e-6, -1)
            depth_hor = (yHor - oy) / sinA
            xHor = ox + depth_hor * cosA

            deltaDepth = dy / sinA
            dx = deltaDepth * cosA

            for i in range(MAX_DEPTH):
                tileHor = int(xHor), int(yHor)
                if tileHor in self.map.worldMap:
                    self.textureHor = self.map.worldMap[tileHor]
                    #print("s")
                    break
                xHor += dx
                yHor += dy
                depth_hor += deltaDepth

            # vert
            xvert, dx = (xMap + 1, 1) if cosA > 0 else (xMap - 1e-6, -1)

            depth_vert = (xvert - ox) / cosA
            yvert = oy + depth_vert * sinA

            deltaDepth = dx / cosA
            dy = deltaDepth * sinA

            for i in range(MAX_DEPTH):
                tileVert = int(xvert), int(yvert)
                if tileVert in self.map.worldMap:
                    self.textureVert = self.map.worldMap[tileVert]
                    break
                xvert += dx
                yvert += dy
                depth_vert += deltaDepth

            # depth
            if depth_vert < depth_hor:
                depth = depth_vert
                yvert %= 1
                texture = self.textureVert
                offset = yvert if cosA > 0 else (1 - yvert)
            else:
                depth = depth_hor
                xHor %= 1
                texture = self.textureHor
                offset = (1 - xHor) if sinA > 0 else xHor

            # remove fishbowl effect
            depth *= math.cos(self.runner.player.angle - angleA)

            # projection
            projHeight = SCREEN_DIST / (depth + 0.00001)

            self.rayCastingResult.append(
                (depth, projHeight, texture, offset)
            )

            angleA += DELTA_ANGLE
    
    def update(self):
        self.rayCast()
        self.getObjectToRender()