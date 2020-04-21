import tkinter as tk                # python 3
from tkinter import font as tkfont # python 3
from tkinter import *

class BSS_App(Tk):

    def __init__(self):
        Tk.__init__(self)
        container = tk.Frame(self)
        self.app_data = {"UUID": StringVar(),
                         "Connection_status": StringVar()
                         }
        container.pack(side="top", fill="both", expand = True)
        self.frames = {}
        for F in (PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky = NSEW)
        self.show_frame(PageOne)
        

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        tk.Label(self, text='PageOne').grid(padx=(20,20), pady=(20,20))
        self.make_widget(controller)

    def make_widget(self, controller):
        self.some_input = StringVar
        self.some_entry = tk.Entry(self, textvariable=self.controller.app_data["UUID"], width=8) 
        self.some_entry.grid()
        button1 = tk.Button(self, text='Next Page',
                                  command=lambda: controller.show_frame(PageTwo))
        button1.grid()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        tk.Label(self, text='PageTwo').grid(padx=(20,20), pady=(20,20))
        button1 = tk.Button(self, text='Previous Page',
                             command=lambda: controller.show_frame(PageOne))
        button1.grid()
        button2 = tk.Button(self, text='press to print', command=self.print_it)
        button2.grid()

    def print_it(self):
        value = self.controller.app_data["UUID"].get()
        tk.Label(self, text="%s"% value).grid(padx=(30,30), pady=(30,30))
        print(value)
        #What do I put here 
        #to print the value of some_input from PageOne

app = BSS_App()
app.title('Multi-Page Test App')
app.mainloop()