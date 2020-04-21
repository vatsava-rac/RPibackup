from tkinter import *

gui = Tk()

gui.geometry("800x800")

#Create label
usr_id_lbl = Label(gui,text = "Vehicle Id").place(x = 260, y = 50)

#Create entry
usr_id_entry = Entry(gui,width = 25).place(x = 350, y = 50)

#create confirm button
cnfm_btn = Button(gui,text = "Confirm", activebackground = "dodger blue", activeforeground = "black").place(x = 300, y = 90)

#create cancel button
cncl_btn = Button(gui,text = "Cancel", activebackground = "dodger blue", activeforeground = "black").place(x = 430, y = 90)


gui.mainloop()