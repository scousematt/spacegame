import tkinter as tk
import tkinter.ttk as ttk

import canvasSystem
import canvasFaction
import canvasMenu
import game

import game

LARGE_FONT = ("Verdana", 12)


class SpaceGame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)




        container = tk.Frame(self)

        container.pack(side = "top", fill="both", expand= True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        game.top_menu = (StartPage, canvasSystem.PageOne, canvasFaction.PageOne)
        for F in game.top_menu:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(canvasMenu.GameFrame):

    def __init__(self, parent, controller):
        canvasMenu.GameFrame.__init__(self, parent, controller)

        self.game = parent
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="System Data",
                            command=lambda: controller.show_frame(canvasSystem.PageOne))
        button1.pack()
