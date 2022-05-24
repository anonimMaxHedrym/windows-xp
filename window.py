from sqlite3 import Row
import arcade
import os
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
SCREEN_TITLE = "windows xp"

class Object(arcade.Sprite):
    def __init__(self, image, size):
        super().__init__(image, size)
    def standing(self, center_x, center_y, row, column):
        self.set_position(center_x, center_y)
        self.row = row
        self.column = column

class Papka(Object):
    def __init__(self):
        super().__init__("papka.png", 0.5)
        self.center_x = 700
        self.center_y = 600

class Bush(Object):
    def __init__(self):
        super().__init__("bush1 (1).png", 0.2)
        self.center_x = 500
        self.center_y = 600

class Yandex(Object):
    def __init__(self):
        super().__init__("yandex.png", 0.2)
        self.center_x = 300
        self.center_y = 600



class Comp(Object):
    def __init__(self):
        super().__init__("wind.png", 0.5)
        self.center_x = 100
        self.center_y = 600
        self.name = "comp"

class MyWindow(arcade.Window):
    def __int__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("fon.jpg")
        self.comp = Comp()



    def setup(self):
        self.touch = None

    def on_draw(self):
        self.clear()
        self.bg = arcade.load_texture("fon.jpg")
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.comp = Comp()
        self.comp.draw()
        if self.touch != None:
            self.touch.draw()
        self.yandex = Yandex()
        self.yandex.draw()
        self.bush = Bush()
        self.bush.draw()
        self.papka = Papka()
        self.papka.draw()


    def on_mouse_press(self, x, y, buttom, modifiers):
        if 16 <= x <= 116:
            if 600 <= y <= 680:
                self.touch = Comp()
                print(self.touch.name)
        if self.touch != None:
            self.touch.center_x = x
            self.touch.center_y = y
            self.touch.alpha = 150


    def on_mouse_release(self, x, y, buttom, modifires):

        self.touch.alpha = 225
        if self.touch.name == "comp":
            self.comp.center_x = self.touch.center_x
            self.comp.center_y = self.touch.center_y
#            print("test")


        


window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()