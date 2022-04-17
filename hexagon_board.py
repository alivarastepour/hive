import tkinter
from pydoc import text
from tkinter import TOP, LEFT, RIGHT, BOTTOM, BOTH, ttk, Y, END
from turtle import Canvas
import math
from tkinter.ttk import *
from gameInstance import game


class Field:
    def __init__(self, parent, x, y, kind, size):
        self.parent = parent
        self.x = x
        self.y = y
        self.kind = kind
        self.color = "#00FFFF"
        # Field.types[self.kind]
        self.selected = False

    def draw(self):
        FillHexagon(self.parent, self.x, self.y, self.size, self.color)

    def enlight(self):
        pass


# ------------------------------------------------------------------------------
class StrokeHexagon:
    def __init__(self, parent, x, y, length, color):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.y = y  # top left y
        self.length = length  # length of a side
        self.color = color  # outline color

        self.draw()

    def draw(self):
        start_x = self.x
        start_y = self.y
        angle = 60

        for i in range(6):
            end_x = start_x + self.length * math.cos(math.radians(angle * i))
            end_y = start_y + self.length * math.sin(math.radians(angle * i))
            self.parent.create_line(start_x,
                                    start_y,
                                    end_x,
                                    end_y,
                                    fill=self.color)
            start_x = end_x
            start_y = end_y


# ------------------------------------------------------------------------------
class FillHexagon:
    def __init__(self, parent, x, y, length, color, tags):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.y = y  # top left y
        self.length = length  # length of a side
        self.color = color  # fill color
        self.selected = False
        self.tags = tags

        self.draw()

    def draw(self):
        start_x = self.x
        start_y = self.y
        angle = 60
        coords = []
        for i in range(6):
            end_x = start_x + self.length * math.cos(math.radians(angle * i))
            end_y = start_y + self.length * math.sin(math.radians(angle * i))
            coords.append([start_x, start_y])
            start_x = end_x
            start_y = end_y
        self.parent.create_polygon(coords[0][0],
                                   coords[0][1],
                                   coords[1][0],
                                   coords[1][1],
                                   coords[2][0],
                                   coords[2][1],
                                   coords[3][0],
                                   coords[3][1],
                                   coords[4][0],
                                   coords[4][1],
                                   coords[5][0],
                                   coords[5][1],
                                   fill=self.color,
                                   outline="gray",
                                   tags=self.tags)


# ---------------------------------------------------------
def open_window_for_insect_selection(insect_selection_window):
    insect_selection_window = tkinter.Toplevel(app)
    insect_selection_window.title("Insect Selection")
    insect_selection_window.geometry("400x800")
    Label(insect_selection_window, text='Select the insect you want', font=('Verdana', 12)).pack(side=TOP, pady=10)

    pane = Frame(insect_selection_window)
    pane.pack(fill=BOTH, expand=True)

    # queen information
    lbl_queen_count = tkinter.Label(
        master=pane,
        text=1,
        width=15,
        height=6,
        borderwidth=1, relief="solid"
    )
    lbl_queen_count.place(x=250, y=0)
    queenPhoto_btn = tkinter.PhotoImage(file="./assets/queen.png", )
    queenPhoto_btn = queenPhoto_btn.zoom(21)
    queenPhoto_btn = queenPhoto_btn.subsample(50)
    Button(pane, image=queenPhoto_btn, command=lambda: minus_1_queen()).place(x=50, y=0)

    # ant information
    lbl_ant_count = tkinter.Label(
        master=insect_selection_window,
        text=3,
        width=15,
        height=6,
        borderwidth=1, relief="solid"
    )
    lbl_ant_count.place(x=250, y=167)
    antPhoto_btn = tkinter.PhotoImage(file="./assets/ant.png")
    antPhoto_btn = antPhoto_btn.zoom(22)
    antPhoto_btn = antPhoto_btn.subsample(50)
    Button(pane, image=antPhoto_btn, command=lambda: minus_1_ant()).place(x=50, y=120)

    # beetle information
    beetlePhoto_btn = tkinter.PhotoImage(file="./assets/beetle.png")
    beetlePhoto_btn = beetlePhoto_btn.zoom(19)
    beetlePhoto_btn = beetlePhoto_btn.subsample(52)
    Button(pane, image=beetlePhoto_btn , command = lambda : minus_1_beetle()).place(x=50, y=300)
    lbl_beetle_count = tkinter.Label(
        master=insect_selection_window,
        text=2,
        width=15,
        height=6,
        borderwidth=1, relief="solid"
    )
    lbl_beetle_count.place(x=250, y=325)

    # spider information
    spiderPhoto_btn = tkinter.PhotoImage(file="./assets/spider.png")
    spiderPhoto_btn = spiderPhoto_btn.zoom(28)
    spiderPhoto_btn = spiderPhoto_btn.subsample(40)
    Button(pane, image=spiderPhoto_btn , command = lambda : minus_1_spider()).place(x=50, y=450)
    lbl_spider_count = tkinter.Label(
        master=insect_selection_window,
        text=2,
        width=15,
        height=6,
        borderwidth=1, relief="solid"
    )
    lbl_spider_count.place(x=250, y=500)

    # grasshopper information
    grasshoperPhoto_btn = tkinter.PhotoImage(file="./assets/grasshoper.png")
    grasshoperPhoto_btn = grasshoperPhoto_btn.zoom(20)
    grasshoperPhoto_btn = grasshoperPhoto_btn.subsample(50)
    Button(pane, image=grasshoperPhoto_btn , command = lambda : minus_1_grasshopper()).place(x=50, y=600)
    lbl_grasshoper_count = tkinter.Label(
        master=insect_selection_window,
        text=3,
        width=15,
        height=6,
        borderwidth=1, relief="solid"
    )
    lbl_grasshoper_count.place(x=250, y=640)

    def minus_1_queen():
        if lbl_queen_count['text'] >= 1:
            lbl_queen_count['text'] = lbl_queen_count['text'] - 1
            print("Queen is chosen")
        else:
            print("You can't choose this insect")

    def minus_1_ant():
        if lbl_ant_count['text'] >= 1:
            lbl_ant_count['text'] = lbl_ant_count['text'] - 1
            print("Ant is chosen")
        else:
            print("You can't choose this insect")

    def minus_1_beetle():
        if lbl_beetle_count['text'] >= 1:
            lbl_beetle_count['text'] = lbl_beetle_count['text'] - 1
            print("Beetle is chosen")
        else:
            print("You can't choose this insect")

    def minus_1_spider():
        if lbl_spider_count['text'] >= 1:
            lbl_spider_count['text'] = lbl_spider_count['text'] - 1
            print("Spider is chosen")
        else:
            print("You can't choose this insect")

    def minus_1_grasshopper():
        if lbl_grasshoper_count['text'] >= 1:
            lbl_grasshoper_count['text'] = lbl_grasshoper_count['text'] - 1
            print("Grasshopper is chosen ")
        else:
            print("You can't choose this insect")

    pane.mainloop()


# def button_got_clicked():
# print("fuck u")


class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Hive")
        self.can = Canvas(self, width=660, height=1000, bg="#66CDAA")
        self.can.pack()

        self.hexagons = []
        self.initGrid(22, 22, 20, debug=False)

        self.can.bind("<Button-1>", self.click)

    def initGrid(self, cols, rows, size, debug):
        """
        2d grid of hexagons
        """
        for c in range(cols):
            if c % 2 == 0:
                offset = size * math.sqrt(3) / 2
            else:
                offset = 0
            for r in range(rows):

                h = FillHexagon(self.can,
                                c * (size * 1.5),
                                (r * (size * math.sqrt(3))) + offset,
                                size,
                                "#60ace6",
                                "{}.{}".format(r, c))
                self.hexagons.append(h)

                if debug:
                    coords = "{}, {}".format(r, c)
                    self.can.create_text(c * (size * 1.5) + (size / 2),
                                         (r * (size * math.sqrt(3))) + offset + (size / 2),
                                         text=coords)

    def click(self, evt):
        """
        hexagon detection on mouse click
        """
        x, y = evt.x, evt.y
        for i in self.hexagons:
            i.selected = False
            i.isNeighbour = False
            self.can.itemconfigure(i.tags, fill=i.color)
        clicked = self.can.find_closest(x, y)[0]  # find closest
        self.hexagons[int(clicked) - 1].selected = True
        game.selectedHexagon = (clicked % 22 - 1, clicked // 22)
        # print(f"x: {clicked % 22 -1 }, y: {clicked // 22} selected.")
        for i in self.hexagons:  # re-configure selected only
            if i.selected:
                self.can.itemconfigure(i.tags, fill="#00FFFF")
            if i.isNeighbour:
                self.can.itemconfigure(i.tags, fill="#76d576")
        open_window_for_insect_selection(app)


# ----------------------------------------------------------


if __name__ == '__main__':
    app = App()
    app.mainloop()
