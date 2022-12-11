import tkinter as tk
from tkinter import ttk as ttk
from tkinter import font as tkfont 

input_val = ''


class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, InputPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.currentframe = self.frames['MainMenu']

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        self.currentframe = self.frames[page_name]
        try:
            self.currentframe.tkraise()
        except:
            self.currentframe.input.set('exit')
            self.send()
    
    def send(self, *args):
        if args.__len__() > 0:
            try:
                self.currentframe.input.set(args[0])
            except AttributeError:
                pass
        self.quit()
    
    def on_closing(self, *args):
        self.currentframe.input.set('exit')
        self.send()

    def get_input(self, label_text = "This is the input page"):
        self.currentframe.label.text = label_text
        self.mainloop()
        i = self.currentframe.input.get()
        self.currentframe.input.set('')
        return i

class InputPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="This is the input page", font=self.controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.input = tk.StringVar()
        self.input_entry = ttk.Entry(self, width=7, textvariable=self.input)
        self.input_entry.pack()

        self.enterbutton = ttk.Button(self, text="ENTER", command=self.controller.send)
        self.enterbutton.pack()
        

        # button1 = tk.Button(self, text="Go to Page One",
        #                     command=lambda: controller.show_frame("PageOne"))
        # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("PageTwo"))
        # button1.pack()
        # button2.pack()


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.label = tk.Label(self, text="This is page 1", font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.input = tk.StringVar()

        buttons = [
            tk.Button(
                self, 
                text="new game",
                command=lambda: controller.send('new game')),
            tk.Button(
                self, 
                text="load game",
                command=lambda: controller.send('load game')),
            tk.Button(
                self, 
                text="exit",
                command=lambda: controller.send('exit'))
            ]

        for button in buttons:
            button.pack()

frames = [
    {
        "__name__": "InputPage",
        "label": {
            "definition": {
                "class": tk.Label,
                "args": [],
                "kwargs": {
                    "text": "This is the input page",
                    "font": "self.controller.title_font"
                }
            },

            "fun": {
                "pack": {
                    "args": [],
                    "kwargs": {
                        "side": "top",
                        "fill": "x",
                        "pady": 10
                    }
                }
            }
        },
        "input": {
            "definition": {
                "class": tk.StringVar,
                "args": [],
                "kwargs": {}
            },

            "fun": {}
        },
        "input_entry": {
            "definition": {
                "class": ttk.Entry,
                "args": [],
                "kwargs": {
                    "width":7, 
                    "textvariable": "self.input"
                }
            },

            "fun": {
                "pack": {
                    "args": [],
                    "kwargs": {}
                }
            }
        },
        "enterbutton": {
            "definition": {
                "class": ttk.Button,
                "args": [],
                "kwargs": {
                    "text": "ENTER", 
                    "command": "self.controller.send"
                }
            },

            "fun": {
                "pack": {
                    "args": [],
                    "kwargs": {}
                }
            }
        }
    },
    {

    }
]

if __name__ == "__main__":
    gui = GUI()
    while True:
        print(gui.get_input)