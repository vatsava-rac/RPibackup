import tkinter as tk                # python 3
from tkinter import font as tkfont # python 3
from tkinter import *

class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title_font = tkfont.Font(family='Futura Bk BT', size=18)
        self.geometry('900x600')
        self.title("RACEnergy Battery Swapping Station")
        
        self.app_data = {"UUID": StringVar(),
                         "Connection_status": StringVar()
                         }
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (StartPage1, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage1")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    
    
class StartPage1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="RACEnergy BSS", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
#Entering Kit ID (Manual Input 1)
        lbl0 = tk.Label(self, text="Enter Kit ID", font=("Futura Bk BT", 12))
        lbl0.place(x=310, y=110, anchor="w")
#Text box for recieving entry
        self.uid_input = tk.Entry(self,textvariable=self.controller.app_data["UUID"],width=25)
        self.uid_input.place(x=430, y=110, anchor="w")
        self.uid_input.focus()
        #OK and Cancel buttons
        btn0 = tk.Button(self, text="OK",
                            command=lambda: controller.show_frame("PageOne"))
        btn0.place(x=410, y=150, anchor="center")
        
        btn1 = tk.Button(self, text="Cancel")
        btn1.place(x=480, y=150, anchor="center")
        
#Home Button
        btn2 = tk.Button(self, text = "Home",
                            command=lambda: controller.show_frame("StartPage1"))     
        btn2.place(x=850, y=30, anchor="center")     

################################################################################
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        UUID = self.controller.app_data["UUID"].get()
        lbl1 = tk.Label(self, text="Swapping with Kit ID: %s" % (UUID), font=controller.title_font)
        print (UUID)
        lbl1.pack(side="top", fill="x", pady=10)

        #Connection status variable:
        connection = StringVar()
        connection.set("Connected") #assign value
        lbl = tk.Label(self, text="Connection Status:  %s" % (connection.get()), font=("Futura Bk BT", 8))
        lbl.place(x=20, y=85, anchor="w")
        
#Displaying details:
        #Vehicle Number variable:
        vno = StringVar()
        vno.set("2019RE00001") #assign value
        lbl2 = tk.Label(self, text="Vehicle Number:    %s " % (vno.get()), font=("Futura Bk BT", 12))
        lbl2.place(x=310, y=150, anchor="w")

        #SoC variable:
        soc = IntVar()
        soc.set("80") #assign value
        lbl3 = tk.Label(self, text="SoC of the Pack:    %d %%" %(soc.get()), font=("Futura Bk BT", 12))
        lbl3.place(x=310, y=175, anchor="w")

        #Energy used variable:
        energy = DoubleVar()
        energy.set("5.80") #assign value
        lbl4 = tk.Label(self, text="Energy Used:        %.2f kWh" % (energy.get()), font=("Futura Bk BT", 12))
        lbl4.place(x=310, y=200, anchor="w")


        #Bill amount variable:
        bill = IntVar()
        bill.set("189") #assign value
        lbl5 = tk.Label(self, text="Bill Amount:          INR %.2f" % (bill.get()), font=("Futura Bk BT", 12))
        lbl5.place(x=310, y=225, anchor="w")

#Payment Button
        btn2 = tk.Button(self, text = "Bill Paid",
                            command=lambda: controller.show_frame("PageTwo"))     
        btn2.place(relx = 0.5, rely=0.5, anchor="center")

        
#Home Button
        btn2 = tk.Button(self, text = "Home",
                            command=lambda: controller.show_frame("StartPage1"))     
        btn2.place(x=850, y=30, anchor="center")

################################################################################
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Swap Batteries", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        #Bill amount variable:
        bssLatch = StringVar()
        bssLatch.set("Open") #assign value
        lbl5 = tk.Label(self, text="BSS Latch Status:        %s" % (bssLatch.get()), font=("Futura Bk BT", 12))
        lbl5.place(x=310, y=150, anchor="w")

        #Bill amount variable:
        kitLatch = StringVar()
        kitLatch.set("Open") #assign value
        lbl6 = tk.Label(self, text="Kit Latch Status:          %s" % (kitLatch.get()), font=("Futura Bk BT", 12))
        lbl6.place(x=310, y=175, anchor="w")

        #Swapping status variable:
        swap = StringVar()
        swap.set("Open") #assign value
        lbl7 = tk.Label(self, text="Swapping Status:      %s" % (swap.get()), font=("Futura Bk BT", 12))
        lbl7.place(x=310, y=200, anchor="w")

#Finish Button
        btn2 = tk.Button(self, text = "Finish",
                            command=lambda: controller.show_frame("StartPage1"))     
        btn2.place(relx = 0.5, rely=0.5, anchor="center")
        
#Home Button
        btn2 = tk.Button(self, text = "Home",
                            command=lambda: controller.show_frame("StartPage1"))     
        btn2.place(x=850, y=30, anchor="center")

#if __name__ == "__main__":
app = SampleApp()
app.title('BSS')
app.mainloop()