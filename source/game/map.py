import pygame as pg
from ..db import DB

class MiniMap:
    def __init__(self, game) -> None:
        self.game = game
        db = DB()
        db.load()
        data = db.data
        self.game = game
        self.miniMap = data["levels"][str(data["cLevel"])]["map"]
        print(self.miniMap)
        self.worldMap = {}
        self.getMap()

    def getMap(self):
        for j, row in enumerate(self.miniMap):
            for i, value in enumerate(row):
                #print(value)
                if value > 0:
                    self.worldMap[(i, j)] = value
    
    def draw(self):
        [pg.draw.rect(self.game.screen, (0, 0, 0), (pos[0]*100, pos[1]*100, 100, 100), 2) for pos in self.worldMap]