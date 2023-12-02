import pygame as pg
from ..font import Font, init

init()

class Home:
    running = False
    name = "home"
    def __init__(self, app):
        self.window:pg.Surface = app.window
        self.font = Font("./assest/font/en.ttf", 40)
        self.app = app
    
    def draw(self):
        length = len(self.app.apps)
        mouse = pg.mouse.get_pos()
        for i, app in enumerate(self.app.apps):
            if str(app) == self.name:
                continue
            txt = self.font.render(app, (255,255,255))

            x = self.window.get_width()/2-txt.get_width()/2
            y = self.window.get_height()/length*(i)

            rect = pg.Rect(
                self.window.get_width()/2-100,
                y-3, 
                200, txt.get_height()+6
            )

            color = (51,51,51)
            if rect.collidepoint(mouse):
                color = (31,31,31)
                if pg.mouse.get_pressed()[0]:
                    self.running = False
                    self.app.apps[app].running = True

            pg.draw.rect(
                self.window,
                color,
                rect, border_radius=3
            )
            self.window.blit(txt,(x, y))

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:self.app.running = False

    def loop(self):
        if not self.running:
            return
        self.draw()
        self.update()