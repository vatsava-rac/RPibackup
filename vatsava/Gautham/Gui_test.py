import tkinter as tk                # python 3
from tkinter import font as tkfont # python 3
from tkinter import *

global UID_txt_box
global kit_id


    
class Screen1(tk.Frame):

    def __init__(root, parent, controller):
        tk.Frame.__init__(root, parent)
        root.controller = controller
        
        label = tk.Label(root, text="RACEnergy BSS", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
#Entering Kit ID (Manual Input 1)
        lbl0 = tk.Label(root, text="Enter Kit ID", font=("Futura Bk BT", 12))
        lbl0.place(x=310, y=110, anchor="w")
#Text box for recieving entry
        UID_txt_box = tk.Entry(root,width=25)
        UID_txt_box.place(x=430, y=110, anchor="w")
        UID_txt_box.focus()
        #OK and Cancel buttons
        ok_btn = tk.Button(root, text="OK",command = lambda: controller.show_frame("Screen2"))
        ok_btn.place(x=410, y=150, anchor="center")
        
        cncl_btn = tk.Button(root, text="Cancel")
        cncl_btn.place(x=480, y=150, anchor="center")
        
#Home Button
        btn2 = tk.Button(root, text = "Home",
                            command=lambda: controller.show_frame("Screen1"))     
        btn2.place(x=850, y=30, anchor="center")
        global kitid
        kitid = UID_txt_box.get()
        print (kitid)

################################################################################
class Screen2(tk.Frame):

    def __init__(root, parent, controller):
        tk.Frame.__init__(root, parent)
        root.controller = controller
        
        lbl1 = tk.Label(root, text="Swapping with Kit ID:", font=controller.title_font)
        lbl1.pack(side="top", fill="x", pady=10)

        #Connection status variable:
        connection = StringVar()
        connection.set("Connected") #assign value
        lbl = tk.Label(root, text="Connection Status:  %s" % (connection.get()), font=("Futura Bk BT", 8))
        lbl.place(x=20, y=85, anchor="w")
        
#Displaying details:
        #Vehicle Number variable:
        vno = StringVar()
        vno.set("2019RE00001") #assign value
        lbl2 = tk.Label(root, text="Vehicle Number:    %s " % (vno.get()), font=("Futura Bk BT", 12))
        lbl2.place(x=310, y=150, anchor="w")

        #SoC variable:
        soc = IntVar()
        soc.set("80") #assign value
        lbl3 = tk.Label(root, text="SoC of the Pack:    %d %%" %(soc.get()), font=("Futura Bk BT", 12))
        lbl3.place(x=310, y=175, anchor="w")

        #Energy used variable:
        energy = DoubleVar()
        energy.set("5.80") #assign value
        lbl4 = tk.Label(root, text="Energy Used:        %.2f kWh" % (energy.get()), font=("Futura Bk BT", 12))
        lbl4.place(x=310, y=200, anchor="w")


        #Bill amount variable:
        bill = IntVar()
        bill.set("189") #assign value
        lbl5 = tk.Label(root, text="Bill Amount:          INR %.2f" % (bill.get()), font=("Futura Bk BT", 12))
        lbl5.place(x=310, y=225, anchor="w")

#Payment Button
        btn2 = tk.Button(root, text = "Bill Paid",
                            command=lambda: controller.show_frame("Screen3"))     
        btn2.place(relx = 0.5, rely=0.5, anchor="center")

        
#Home Button
        btn2 = tk.Button(root, text = "Home",
                            command=lambda: controller.show_frame("Screen1"))     
        btn2.place(x=850, y=30, anchor="center")

################################################################################
class Screen3(tk.Frame):

    def __init__(root, parent, controller):
        tk.Frame.__init__(root, parent)
        root.controller = controller
        label = tk.Label(root, text="Swap Batteries", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        #Bill amount variable:
        bssLatch = StringVar()
        bssLatch.set("Open") #assign value
        lbl5 = tk.Label(root, text="BSS Latch Status:        %s" % (bssLatch.get()), font=("Futura Bk BT", 12))
        lbl5.place(x=310, y=150, anchor="w")

        #Bill amount variable:
        kitLatch = StringVar()
        kitLatch.set("Open") #assign value
        lbl6 = tk.Label(root, text="Kit Latch Status:          %s" % (kitLatch.get()), font=("Futura Bk BT", 12))
        lbl6.place(x=310, y=175, anchor="w")

        #Swapping status variable:
        swap = StringVar()
        swap.set("Open") #assign value
        lbl7 = tk.Label(root, text="Swapping Status:      %s" % (swap.get()), font=("Futura Bk BT", 12))
        lbl7.place(x=310, y=200, anchor="w")

#Finish Button
        btn2 = tk.Button(root, text = "Finish",
                            command=lambda: controller.show_frame("Screen1"))     
        btn2.place(relx = 0.5, rely=0.5, anchor="center")
        
#Home Button
        btn2 = tk.Button(root, text = "Home",
                            command=lambda: controller.show_frame("Screen1"))     
        btn2.place(x=850, y=30, anchor="center")
        
root = Tk()
root.title_font = tkfont.Font(family='Futura Bk BT', size=18)
root.geometry('900x600')
root.title("RACEnergy Battery Swapping Station")

container = tk.Frame(root)
container.pack(side="top", fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

root.frames = {}

for F in (Screen3, Screen2, Screen1):
    screen_name = F.__name__
    frame = F(parent=container, controller=root)
    root.frames[screen_name] = frame

    # put all of the pages in the same location;
    # the one on the top of the stacking order
    # will be the one that is visible.
    frame.grid(row=0, column=0, sticky="nsew")

def show_frame(root, screen_name):
#         '''Show a frame for the given page name'''
#         frame = root.frames[screen_name]
#         frame.tkraise()
    kit_id = UID_txt_box.get()
    print (kit_id)
    root.destroy()


if __name__ == "__main__":
    app.mainloop()