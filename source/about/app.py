import pygame as pg
from ..font import Font, init
init()

class Info:
    texts:list[pg.Surface] = []
    text = """سلام به تو بازیکن عزیز
امیدوارم نهایت لذت رو از این بازی ببری

طراح تصویر و شخصیت : سپهر طاهرخانی
برنامه نویس : محمد صدرا گرجی"""
    offset = 0
    running = False
    def __init__(self, app) -> None:
        self.app = app
        self.window:pg.Surface = app.window
        self.font = Font("./assest/font/fa.ttf", 50)
        for text in self.text.split("\n"):
            self.texts.append(
                self.font.render(
                    text, (255,255,255)
                )
            )

    def draw(self):
        for index, surface in enumerate(self.texts):
            index+=1
            self.window.blit(
                surface,
                (
                    self.window.get_width()/2-surface.get_width()/2,
                    index*surface.get_height()+40
                )
            )

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.app.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                    self.app.apps["home"].running = True

    def loop(self):
        if not self.running:
            return
        self.update()
        self.draw()