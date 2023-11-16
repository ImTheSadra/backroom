import pygame as pg

_ = False

miniMap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class MiniMap:
    def __init__(self, game) -> None:
        self.game = game
        self.miniMap = miniMap
        self.worldMap = {}
        self.getMap()

    def getMap(self):
        for j, row in enumerate(self.miniMap):
            for i, value in enumerate(row):
                #print(value)
                if value == 1:
                    self.worldMap[(i, j)] = value
    
    def draw(self):
        [pg.draw.rect(self.game.screen, (0, 0, 0), (pos[0]*100, pos[1]*100, 100, 100), 2) for pos in self.worldMap]