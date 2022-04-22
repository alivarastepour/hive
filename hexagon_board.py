import tkinter
from pydoc import text
from tkinter import TOP, LEFT, RIGHT, BOTTOM, BOTH, ttk, Y, END
from turtle import Canvas
import math
from tkinter.ttk import *
from gameInstance import game
from userInstance import *
from constants import *
from neighborhoodUtil import *


def changeTurn():
    if game.turn == 1:
        game.turn = 2
    else:
        game.turn = 1


class Field:
    def __init__(self, parent, x, y, kind, size):
        self.parent = parent
        self.x = x
        self.y = y
        self.kind = kind
        self.color = "#00FFFF"
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
        self.label = None
        self.piece_color = 'white'

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
def open_window_for_insect_selection(insect_selection_window, self):
    main_window = insect_selection_window
    insect_selection_window = tkinter.Toplevel(app)
    insect_selection_window.title("Insect Selection")
    insect_selection_window.geometry("400x800")
    Label(insect_selection_window, text='Select the insect you want', font=('Verdana', 12)).pack(side=TOP, pady=10)

    pane = Frame(insect_selection_window)
    pane.pack(fill=BOTH, expand=True)
    exit_BTN = Button(insect_selection_window, text="Quit", command=insect_selection_window.destroy)
    exit_BTN.place(x=80, y=10)

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
    Button(pane, image=queenPhoto_btn, command=lambda: minus_1_queen(*game.selectedHexagon, main_window)).place(x=50,
                                                                                                                y=0)

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
    Button(pane, image=antPhoto_btn, command=lambda: minus_1_ant(*game.selectedHexagon, main_window)).place(x=50, y=120)

    # beetle information
    beetlePhoto_btn = tkinter.PhotoImage(file="./assets/beetle.png")
    beetlePhoto_btn = beetlePhoto_btn.zoom(19)
    beetlePhoto_btn = beetlePhoto_btn.subsample(52)
    Button(pane, image=beetlePhoto_btn, command=lambda: minus_1_beetle(*game.selectedHexagon, main_window)).place(x=50,
                                                                                                                  y=300)
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
    Button(pane, image=spiderPhoto_btn, command=lambda: minus_1_spider(*game.selectedHexagon, main_window)).place(x=50,
                                                                                                                  y=450)
    lbl_spider_count = tkinter.Label(
        master=insect_selection_window,
        text=2,
        width=15,
        height=6,
        borderwidth=1, relief="solid"
    )
    lbl_spider_count.place(x=250, y=500)

    # grasshopper information
    grasshopperPhoto_btn = tkinter.PhotoImage(file="./assets/grasshoper.png")
    grasshopperPhoto_btn = grasshopperPhoto_btn.zoom(20)
    grasshopperPhoto_btn = grasshopperPhoto_btn.subsample(50)
    Button(pane, image=grasshopperPhoto_btn,
           command=lambda: minus_1_grasshopper(*game.selectedHexagon, main_window)).place(x=50,
                                                                                          y=600)
    lbl_grasshopper_count = tkinter.Label(
        master=insect_selection_window,
        text=3,
        width=15,
        height=6,
        borderwidth=1, relief="solid"
    )
    lbl_grasshopper_count.place(x=250, y=640)

    def define_offset(a, b):
        if b % 2 == 0:
            offset = 20 * math.sqrt(3) / 2
        else:
            offset = 0
        return offset

    def minus_1_queen(x, y, main_window):
        main_window.can.itemconfigure(main_window.hexagons[y * 22 + x].tags, fill='yellow')
        offset = define_offset(x, y)
        if game.turn == 1:
            lbl = self.can.create_text(y * (20 * 1.5) + (20 / 2),
                                 (x * (20 * math.sqrt(3))) + offset + (20 / 2),
                                 text='1')
            self.hexagons[y * 22 + x].label = lbl
            # --------------------------
            self.hexagons[y * 22 + x].piece_color = 'yellow'
            # --------------------------

        elif game.turn == 2:
            lbl = self.can.create_text(y * (20 * 1.5) + (20 / 2),
                                 (x * (20 * math.sqrt(3))) + offset + (20 / 2),
                                 text='2')
            self.hexagons[y * 22 + x].label = lbl
            # --------------------------
            self.hexagons[y * 22 + x].piece_color = 'yellow'
            # --------------------------

        if lbl_queen_count['text'] >= 1:
            lbl_queen_count['text'] = lbl_queen_count['text'] - 1
            print("Queen is chosen")
        else:
            print("You can't choose this insect")
        game.fillHome(game.turn, QUEEN, x, y)
        changeTurn()

    def minus_1_ant(x, y, main_window):
        main_window.can.itemconfigure(main_window.hexagons[y * 22 + x].tags, fill='#ED9121')
        offset = define_offset(x, y)
        if game.turn == 1:
            lbl = self.can.create_text(y * (20 * 1.5) + (20 / 2),
                                 (x * (20 * math.sqrt(3))) + offset + (20 / 2),
                                 text='1')
            self.hexagons[y * 22 + x].label = lbl
            # --------------------------
            self.hexagons[y * 22 + x].piece_color = '#ED9121'
        elif game.turn == 2:
            lbl = self.can.create_text(y * (20 * 1.5) + (20 / 2),
                                 (x * (20 * math.sqrt(3))) + offset + (20 / 2),
                                 text='2')
            self.hexagons[y * 22 + x].label = lbl
            # --------------------------
            self.hexagons[y * 22 + x].piece_color = '#ED9121'
        if lbl_ant_count['text'] >= 1:
            lbl_ant_count['text'] = lbl_ant_count['text'] - 1
            print("Ant is chosen")
        else:
            print("You can't choose this insect")
        game.fillHome(game.turn, ANT, x, y)
        changeTurn()

    def minus_1_beetle(x, y, main_window):
        main_window.can.itemconfigure(main_window.hexagons[y * 22 + x].tags, fill='black')
        offset = define_offset(x, y)
        if game.turn == 1:
            lbl = self.can.create_text(y * (20 * 1.5) + (20 / 2),
                                 (x * (20 * math.sqrt(3))) + offset + (20 / 2),
                                 text='1')
            self.hexagons[y * 22 + x].label = lbl
            # --------------------------
            self.hexagons[y * 22 + x].piece_color = 'black'
        elif game.turn == 2:
            lbl = self.can.create_text(y * (20 * 1.5) + (20 / 2),
                                 (x * (20 * math.sqrt(3))) + offset + (20 / 2),
                                 text='2')
            self.hexagons[y * 22 + x].label = lbl
            # --------------------------
            self.hexagons[y * 22 + x].piece_color = 'black'
        if lbl_beetle_count['text'] >= 1:
            lbl_beetle_count['text'] = lbl_beetle_count['text'] - 1
            print("Beetle is chosen")
        else:
            print("You can't choose this insect")
        game.fillHome(game.turn, BEETLE, x, y)
        changeTurn()

    def minus_1_spider(x, y, main_window):
        main_window.can.itemconfigure(main_window.hexagons[y * 22 + x].tags, fill='#8A360F')
        offset = define_offset(x, y)
        if game.turn == 1:
            lbl = self.can.create_text(y * (20 * 1.5) + (20 / 2),
                                 (x * (20 * math.sqrt(3))) + offset + (20 / 2),
                                 text='1')
            self.hexagons[y * 22 + x].label = lbl
            # --------------------------
            self.hexagons[y * 22 + x].piece_color = '#8A360F'
        elif game.turn == 2:
            lbl = self.can.create_text(y * (20 * 1.5) + (20 / 2),
                                 (x * (20 * math.sqrt(3))) + offset + (20 / 2),
                                 text='2')
            self.hexagons[y * 22 + x].label = lbl
            # --------------------------
            self.hexagons[y * 22 + x].piece_color = '#8A360F'
        if lbl_spider_count['text'] >= 1:
            lbl_spider_count['text'] = lbl_spider_count['text'] - 1
            print("Spider is chosen")
        else:
            print("You can't choose this insect")
        game.fillHome(game.turn, SPIDER, x, y)
        changeTurn()

    def minus_1_grasshopper(x, y, main_window):
        main_window.can.itemconfigure(main_window.hexagons[y * 22 + x].tags, fill='#76EE00')
        offset = define_offset(x, y)
        if game.turn == 1:
            lbl = self.can.create_text(y * (20 * 1.5) + (20 / 2),
                                 (x * (20 * math.sqrt(3))) + offset + (20 / 2),
                                 text='1')
            self.hexagons[y * 22 + x].label = lbl
            # --------------------------
            self.hexagons[y * 22 + x].piece_color = '#76EE00'
        elif game.turn == 2:
            lbl = self.can.create_text(y * (20 * 1.5) + (20 / 2),
                                 (x * (20 * math.sqrt(3))) + offset + (20 / 2),
                                 text='2')
            self.hexagons[y * 22 + x].label = lbl
            # --------------------------
            self.hexagons[y * 22 + x].piece_color = '#76EEE00'
        if lbl_grasshopper_count['text'] >= 1:
            lbl_grasshopper_count['text'] = lbl_grasshopper_count['text'] - 1
            print("Grasshopper is chosen ")
        else:
            print("You can't choose this insect")
        game.fillHome(game.turn, GRASSHOPPER, x, y)
        changeTurn()

    # if game.turn == 1:
    #     game.turn = 2
    # else:
    #     game.turn = 1
    # avail = game.availablePositions()
    # for x, y in avail:
    #     print(x, y)
    #     self.can.itemconfigure(self.hexagons[y * 22 + x].tags, fill='#006400')
    pane.mainloop()


class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Hive")
        self.can = Canvas(self, width=660, height=1000, bg="#66CDAA")
        self.can.pack()
        self.past = []
        self.hexagons = []
        self.initGrid(22, 22, 20, debug=False)
        self.move = False
        self.prev = None
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
                if r == 11 and c == 11:
                    h = FillHexagon(self.can,
                                    c * (size * 1.5),
                                    (r * (size * math.sqrt(3))) + offset,
                                    size,
                                    "#60ace6",
                                    "{}.{}".format(r, c))
                else:
                    h = FillHexagon(self.can,
                                    c * (size * 1.5),
                                    (r * (size * math.sqrt(3))) + offset,
                                    size,
                                    "#fff",
                                    "{}.{}".format(r, c))
                self.hexagons.append(h)

                if debug:
                    coords = "{}, {}".format(r, c)
                    self.can.create_text(c * (size * 1.5) + (size / 2),
                                         (r * (size * math.sqrt(3))) + offset + (size / 2),
                                         text=coords)

    def click(self, evt):
        def define_offset(a, b):
            if b % 2 == 0:
                offset = 20 * math.sqrt(3) / 2
            else:
                offset = 0
            return offset
        # self.past -> rang = default
        for p in self.past:
            clk = p[1] * 22 + p[0]
            self.can.itemconfigure(self.hexagons[clk].tags, fill='white')
        """
        hexagon detection on mouse click
        """
        x, y = evt.x, evt.y
        for i in self.hexagons:
            i.selected = False
            i.isNeighbour = False
        print(x, y)
        clicked = self.can.find_closest(x, y)[0]  # find closest
        # print("clicked : ", clicked)
        print(clicked)
        self.hexagons[int(clicked)].selected = True
        game.selectedHexagon = (clicked % 22 - 1, clicked // 22)
        if game.isFirstMove:
            if game.selectedHexagon != (11, 11):
                return
        if game.isSecondMove:
            if game.selectedHexagon not in getNeighbors(11, 11):
                return
        if not self.move:
            if game.selectedHexagon not in game.availablePositions() and game.selectedHexagon not in game.occupiedHomes.keys():
                print(game.turn, game.availablePositions())
                return
        if game.selectedHexagon in game.occupiedHomes.keys():
            t = game.occupiedHomes.get(game.selectedHexagon)[0]
            print('check', t, game.turn)
            if t != game.turn:
                return
        # print(f"x: {clicked % 22 -1 }, y: {clicked // 22} selected.")
        if self.move:
            if self.prev == game.selectedHexagon:
                self.move = False
                self.prev = None
                return
            isMove = True
            game.changeHome(*game.selectedHexagon, *self.prev)
            if isMove:
                # --------------------------
                prev_color = self.hexagons[self.prev[1] * 22 + self.prev[0]].piece_color
                self.can.itemconfigure(self.hexagons[game.selectedHexagon[1] * 22 + game.selectedHexagon[0]].tags,
                                       fill=prev_color)
                self.hexagons[self.prev[1] * 22 + self.prev[0]].piece_color = 'white'
                self.can.itemconfigure(self.hexagons[self.prev[1] * 22 + self.prev[0]].tags, fill='white')
                self.can.itemconfigure(self.hexagons[game.selectedHexagon[1] * 22 + game.selectedHexagon[0]].tags,
                                       fill=prev_color)
                # --------------------------
                self.can.delete(self.hexagons[self.prev[1] * 22 + self.prev[0]].label)
                offset = define_offset(x, y)
                if game.turn == 1:
                    self.can.create_text(y * (20 * 1.5) + (20 / 2),
                                         (x * (20 * math.sqrt(3))) + offset + (20 / 2),
                                         text='1')
                elif game.turn == 2:
                    self.can.create_text(y * (20 * 1.5) + (20 / 2),
                                         (x * (20 * math.sqrt(3))) + offset + (20 / 2),
                                         text='2')
            self.move = False
            self.prev = None
            print('here')
            if game.turn == 1:
                game.turn = 2
            else:
                game.turn = 1
            return
        if game.selectedHexagon in game.occupiedHomes.keys():
            piece = game.occupiedHomes.get(game.selectedHexagon)[1]
            avail = []
            if piece == GRASSHOPPER:
                avail = game.grasshopperValidMoves(*game.selectedHexagon)
                # game.fillHome(game.turn, piece, x, y)
                for x, y in avail:
                    self.can.itemconfigure(self.hexagons[y * 22 + x].tags, fill='#006400')
                print(avail)
            if piece == QUEEN:
                avail = game.queenValidMoves(*game.selectedHexagon)
                for x, y in avail:
                    self.can.itemconfigure(self.hexagons[y * 22 + x].tags, fill='#006400')
                print(avail)
            if piece == ANT:
                avail = game.antValidMoves(*game.selectedHexagon)
                for x, y in avail:
                    self.can.itemconfigure(self.hexagons[y * 22 + x].tags, fill='#006400')

                print(avail)
            if piece == BEETLE:
                avail = game.beetleValidMoves(*game.selectedHexagon)
                for x, y in avail:
                    self.can.itemconfigure(self.hexagons[y * 22 + x].tags, fill='#006400')
                print(avail)
            if piece == SPIDER:
                avail = game.spiderValidMoves(*game.selectedHexagon)
                for x, y in avail:
                    self.can.itemconfigure(self.hexagons[y * 22 + x].tags, fill='#006400')
                print(avail)
            self.past = avail.copy()
            if avail:
                self.move = True
                self.prev = game.selectedHexagon
        else:
            # avail = game.availablePositions()
            # for x, y in avail:
            #     print(x, y)
            #     self.can.itemconfigure(self.hexagons[y * 22 + x].tags, fill='#006400')
            open_window_for_insect_selection(app, self)
        # print('here')
        # if game.turn == 1:
        #     game.turn = 2
        # else:
        #     game.turn = 1
        # avail = game.availablePositions()
        # for x, y in avail:
        #     print(x, y)
        #     self.can.itemconfigure(self.hexagons[y * 22 + x].tags, fill='#006400')
        # for i in self.hexagons:  # re-configure selected only
        #     if i.selected:
        #         self.can.itemconfigure(i.tags, fill="#00FFFF")
        #     if i.isNeighbour:
        #         self.can.itemconfigure(i.tags, fill="#76d576")


# ----------------------------------------------------------


if __name__ == '__main__':
    app = App()
    app.mainloop()
