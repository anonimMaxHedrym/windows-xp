import os
import arcade
import webbrowser
import tkinter as tk
from tkinter import filedialog



root = tk.Tk()
root.withdraw()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 700
SCREEN_TITLE = "windows xp"
CELL_WIDTH = 150
CELL_HEIGHT = 150

def cell_x(x):
    right_x = 50 + CELL_WIDTH
    column = 1
    while right_x <= x:
        right_x += CELL_WIDTH
        column += 1
    center_x = right_x - CELL_WIDTH / 2
    return center_x, column

def cell_y(y):
    top_y = 50 + CELL_WIDTH
    line = 1
    while top_y <= y:
        top_y += CELL_HEIGHT
        line += 1
    center_y = top_y - CELL_HEIGHT / 2
    return center_y, line




class Object(arcade.Sprite):
    def __init__(self, image, size):
        super().__init__(image, size)
        self.move = False
    def standing(self, center_x, center_y, row, column):
        self.set_position(center_x, center_y)
        self.row = row
        self.column = column

    def long_click( self, delta_time):
        time = 0
        time += delta_time
        if time > 2:
            return True
        else:
            return False

    def get_cords(self):
        y, row = cell_y(self.center_y)
        x, column = cell_x(self.center_x)
        return column, row

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__("h.png", 1)
        self.center_x = 490
        self.center_y = 20

class Calc(Object):
    def __init__(self):
        super().__init__("Calc.png", 0.4)
        self.center_x = 841
        self.center_y = 606


class Pusk(arcade.Sprite):
    def __init__(self):
        super().__init__("pusk.png", 0.14)
        self.center_x = 45
        self.center_y = 20



class Papka(Object):
    def __init__(self):
        super().__init__("papka.png", 0.7)
        self.center_x = 700
        self.center_y = 600


class Bush(Object):
    def __init__(self):
        super().__init__("bush1 (1).png", 0.2)
        self.center_x = 500
        self.center_y = 600


class Googl(Object):
    def __init__(self):
        super().__init__("googl.png", 0.06)
        self.center_x = 300
        self.center_y = 600




class Comp(Object):
    def __init__(self):
        super().__init__("wind.png", 0.5)
        self.center_x = 100
        self.center_y = 600

class MyWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.items_list = []
        self.bg = arcade.load_texture("fon.jpg")
        self.comp = Comp()
        self.papka = Papka()
        self.bush = Bush()
        self.googl = Googl()
        self.pusk = Pusk()
        self.bar = Bar()
        self.calc = Calc()
        self.items_list.append(self.comp.get_cords())
        self.items_list.append(self.papka.get_cords())
        self.items_list.append(self.bush.get_cords())
        self.items_list.append(self.googl.get_cords())
        self.items_list.append(self.calc.get_cords())





    def setup(self):
        self.touch = None

    def on_draw(self):
        self.clear()
        self.bg = arcade.load_texture("fon.jpg")
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)

        self.comp.draw()
        if self.touch != None:
            self.touch.draw()
        self.googl.draw()
        self.bush.draw()
        self.papka.draw()
        self.bar.draw()
        self.pusk.draw()
        self.calc.draw()


    def on_mouse_press(self, x, y, button, modifiers):
        if self.comp.center_x - 30 <= x <= self.comp.center_x + 30 and self.comp.center_y - 30 <= y <= self.comp.center_y + 30 and button == arcade.MOUSE_BUTTON_LEFT:
                self.comp.move = True
                if self.comp.get_cords() in self.items_list:
                    self.items_list.remove(self.comp.get_cords())
        if self.comp.center_x - 30 <= x <= self.comp.center_x + 30 and self.comp.center_y - 30 <= y <= self.comp.center_y + 30 and button == arcade.MOUSE_BUTTON_RIGHT:
            file_path = filedialog.askopenfilename()
        if self.papka.center_x - 30 <= x <= self.papka.center_x + 30 and self.papka.center_y - 30 <= y <= self.papka.center_y + 30 and button == arcade.MOUSE_BUTTON_LEFT:
            self.papka.move = True
            if self.papka.get_cords() in self.items_list:
                self.items_list.remove(self.papka.get_cords())

        if self.papka.center_x - 30 <= x <= self.papka.center_x + 30 and self.papka.center_y - 30 <= y <= self.papka.center_y + 30 and button == arcade.MOUSE_BUTTON_RIGHT:
            file_path = filedialog.askopenfilename()

        if self.bush.center_x - 30 <= x <= self.bush.center_x + 30 and self.bush.center_y - 30 <= y <= self.bush.center_y + 30 and button == arcade.MOUSE_BUTTON_LEFT:
                self.bush.move = True
                if self.bush.get_cords() in self.items_list:
                    self.items_list.remove(self.bush.get_cords())
        if self.bush.center_x - 30 <= x <= self.bush.center_x + 30 and self.bush.center_y - 30 <= y <= self.bush.center_y + 30 and button == arcade.MOUSE_BUTTON_RIGHT:
            file_path = filedialog.askopenfilename(title = "./Корзина")
        if self.googl.center_x - 30 <= x <= self.googl.center_x + 30 and self.googl.center_y - 30 <= y <= self.googl.center_y + 30 and button == arcade.MOUSE_BUTTON_LEFT:
            self.googl.move = True
            if self.googl.get_cords() in self.items_list:
                self.items_list.remove(self.googl.get_cords())
        if self.googl.center_x - 30 <= x <= self.googl.center_x + 30 and self.googl.center_y - 30 <= y <= self.googl.center_y + 30 and button == arcade.MOUSE_BUTTON_RIGHT:

                url = 'https://google.com/'
                webbrowser.open(url)
        if self.calc.center_x - 30 <= x <= self.calc.center_x + 30 and self.calc.center_y - 30 <= y <= self.calc.center_y + 30 and button == arcade.MOUSE_BUTTON_LEFT:
            self.calc.move = True
            if self.calc.get_cords() in self.items_list:
                self.items_list.remove(self.calc.get_cords())

        if self.calc.center_x - 30 <= x <= self.calc.center_x + 30 and self.calc.center_y - 30 <= y <= self.calc.center_y + 30 and button == arcade.MOUSE_BUTTON_RIGHT:
#           calculator.start_calculator()
            os.startfile("E:\Python\windows xp\dist\c.exe")






    def on_mouse_release(self, x, y, buttom, modifires):
        if self.comp.move == True and self.comp.get_cords() not in self.items_list:
            self.comp.center_x, self.comp.column = cell_x(x)
            self.comp.center_y, self.comp.line = cell_y(y)
            self.comp.move = False
            self.comp.alpha = 225
            self.items_list.append((self.comp.column, self.comp.line))
        if self.papka.move == True and self.papka.get_cords() not in self.items_list:
            self.papka.center_x, self.papka.column = cell_x(x)
            self.papka.center_y, self.papka.line = cell_y(y)
            self.papka.move = False
            self.papka.alpha = 225
            self.items_list.append((self.papka.column, self.papka.column))
        if self.bush.move == True and self.bush.get_cords() not in self.items_list:
            self.bush.center_x, self.bush.column = cell_x(x)
            self.bush.center_y, self.bush.line = cell_y(y)
            self.bush.move = False
            self.bush.alpha = 225
            self.items_list.append((self.bush.column, self.bush.line))
        if self.googl.move == True and self.googl.get_cords() not in self.items_list:
            self.googl.center_x, self.googl.column = cell_x(x)
            self.googl.center_y, self.googl.line = cell_y(y)
            self.googl.move = False
            self.googl.alpha = 225
            self.items_list.append((self.googl.column, self.googl.line))
        if self.calc.move == True and self.calc.get_cords() not in self.items_list:
            self.calc.center_x, self.calc.column = cell_x(x)
            self.calc.center_y, self.calc.line = cell_y(y)
            self.calc.move = False
            self.calc.alpha = 225
            self.items_list.append((self.calc.column, self.calc.line))
            print(self.items_list)
            print(self.calc.get_cords())


    def on_mouse_motion(self, x, y, dx, dy):
        if self.comp.move == True:
            self.comp.center_x = x
            self.comp.center_y = y
            self.comp.alpha = 150
            print("test")
#        print(f"x {x} y {y}")
        if self.papka.move == True:
            self.papka.center_x = x
            self.papka.center_y = y
            self.papka.alpha = 150

        if self.bush.move == True:
            self.bush.center_x = x
            self.bush.center_y = y
            self.bush.alpha = 150

        if self.googl.move == True:
            self.googl.center_x = x
            self.googl.center_y = y
            self.googl.alpha = 150

        if self.calc.move == True:
            self.calc.center_x = x
            self.calc.center_y = y
            self.calc.alpha = 150
#           print(" press F")







        


window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()