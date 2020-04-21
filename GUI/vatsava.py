import os
import sys
from tkinter import *
from bluepy.btle import Scanner, DefaultDelegate, UUID, Peripheral
from functools import partial

#usr_inpt    = "TS15UA1266"

gui = Tk()

usr_inpt = StringVar()
vehicle_id   = StringVar()
kit_ble_addr = StringVar()

    
def home():
    gui.geometry("800x800")
    
    gui.title("RACEnergy BSS")
    #Create label
    usr_id_lbl = Label(gui,text = "Vehicle Id").place(x = 260, y = 50)
    #Create entry
    usr_id_entry = Entry(gui,textvariable = usr_inpt,width = 25)
    usr_id_entry.place(x = 350, y = 50)
   #Create label
    status_lbl = Label(gui,text = "Kit status :").place(x=30,y=200)
    ble_stats_val_lbl = Label(gui,text = "Idle")
    ble_stats_val_lbl.place(x=140,y=200)
    
   # TODO: Add documentaion
    cnf_fun = partial(cnf_btn_click,usr_inpt,ble_stats_val_lbl)
    #create confirm button
    cnfm_btn = Button(gui,text = "Confirm",command = cnf_fun, activebackground = "dodger blue", activeforeground = "black")
    cnfm_btn.place(x = 300, y = 90)
    
    cncl_fun = partial(cncl_btn_click,usr_id_entry)
    #create cancel button
    cncl_btn = Button(gui,text = "Cancel", command = cncl_fun, activebackground = "dodger blue", activeforeground = "black")
    cncl_btn.place(x = 430, y = 90)
    #Create reset button
    rst_btn = Button(gui,text = "Reset", command = restart_app, activebackground = "pink", activeforeground = "red")
    rst_btn.pack(side = BOTTOM)
    
def restart_app():
    python = sys.executable
    os.execl(python,python, *sys.argv)

def cnf_btn_click(usr_input, ble_stats):
    vehicle_id = usr_input.get()
    if (vehicle_id != ""):
        if (len(vehicle_id) != 10):
            print("Invalid ID")
        else:
            kit_ble_addr = scan_ble(vehicle_id)
            ble_stats.config(text = 'Scanning...')
            if (kit_ble_addr != None):
                ble_stats.config(text = 'Device found')
                lbl1 = Label(gui,text = "Vehicle Info ").place(x=30,y=250)
                lbl2 = Label(gui,text = "ID                    :").place(x=90,y=280)
                lbl3 = Label(gui,text = "Name              :").place(x=90,y=310)
                lbl4 = Label(gui,text = "Address          :").place(x=90,y=340)
                lbl5 = Label(gui,text = "Energy used   :").place(x=90,y=370)
                lbl4 = Label(gui,text = "Amount(INR)  :").place(x=90,y=400)
                
                lbl2_val = Label(gui,text = vehicle_id).place(x=200,y=280)
                lbl3_val = Label(gui,text = "RACEnergy_1").place(x=200,y=310)
                lbl4_val = Label(gui,text = kit_ble_addr).place(x=200,y=340)
                
                print("Vehicle ID     : ",vehicle_id)
                print("Name           :  RACEnergy_1")
                print("Address        : ",kit_ble_addr)
            else:
                ble_stats.config(text = 'Vehicle not found!!!')
                print("Vehicle not found!!!")              
    else:
        print("ID cannot be empty")
        
def cncl_btn_click(usr_id_entry):
    usr_id_entry.delete(0,END)

def scan_ble(uid):
    scanner = Scanner()
    devices = scanner.scan(3.0)
    for dev in devices:
#print( "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        for (adtype, desc, value) in dev.getScanData():
#print ("  %s = %s" % (desc, value))
            if("Complete Local Name" == desc):
                if(uid == value):
                    return dev.addr
                else:
                    return None    

home()
gui.mainloop()