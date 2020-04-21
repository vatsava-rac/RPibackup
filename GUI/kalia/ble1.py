import os
import sys
from tkinter import *
from bluepy.btle import Scanner, DefaultDelegate, UUID, Peripheral
from functools import partial
from datetime import datetime

#usr_inpt    = "TS15UA1266"
gui = Tk()

usr_inpt = StringVar()
vehicle_id   = StringVar()
kit_ble_addr = StringVar()
   
def home():
    gui.geometry("800x800")
    
    gui.title("RACEnergy BSS")
    #now = datetime.now()
    #current_time = datetime.now("%H:%M")
    #time_now = Label(gui, text = f"{current_time}").place(x = 700,y=10)
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

def latch_status():
    latch_stats = Label(gui,text = "Latch is open")
    latch_stats.place(x=350,y=490)
    end_swap = Button(gui, text = "END SWAP", command = close_swap_file).place(x = 350,y = 450)

#command for END SWAP button.
def close_swap_file():
    all_batteries = open("/home/pi/vatsav/kalia/allpacks.txt", "r")
    bat1 = all_batteries.read()
    all_batteries.close()
    all_batteries = open("/home/pi/vatsav/kalia/allpacks.txt", "w")
    new = bat1.replace("2400","")
    new = new.replace("2500","")
    new = new.replace("2900","")
    print(new)
    all_batteries.write(new)
    all_batteries.close()
    
    charged_batteries = open("/home/pi/vatsav/kalia/fullychargedpacks.txt", "r")
    bat2 = charged_batteries.read()
    charged_batteries.close()
    news = bat2.replace("2400","")
    news = new.replace("2500","")
    news = new.replace("2900","")
    incoming = " 4000 " + "4100 " + "4200"
    charged_batteries = open("/home/pi/vatsav/kalia/fullychargedpacks.txt", "w")
    charged_batteries.write("3000," + "2600")
    charged_batteries.close()
    all_batteries = open("/home/pi/vatsav/kalia/allpacks.txt", "a+")
    all_batteries.write(incoming)
    all_batteries.close()
    
    outgoing_batteries = Label(gui, text = "2400,2500,2600").place(x =200 ,y = 520 )
    incoming_batteries = Label(gui, text = incoming).place(x = 350, y = 520)
    
    ##swap file. It stored the information of the swapped batteries data
    a = datetime.now()
    swap_data = open("swap_data.txt","a+")
    swap_data.write("%s" %a)
    swap_data.write(" Auto is connected\r\n")
    swap_data.write("%s" %a)
    swap_data.write(" ID is ")
    swap_data.write("%s\r\n" %vehicle_id)
    a= datetime.now()
    swap_data.write("%s" %a)
    swap_data.write(" Cost is " + "%s\r\n " %cost)
    swap_data.write("%s" %a + " Energy consumed is " + "%s\r\n" %energy_used)
    swap_data.close()

def cnf_btn_click(usr_input, ble_stats):
    global vehicle_id
    vehicle_id = usr_input.get()
    if (vehicle_id != ""):
        if (len(vehicle_id) != 10):
            print("Invalid ID")
            bottom_label("Invalid ID                ")
        else:
            ble_stats.config(text = "Scanning...")
            kit_ble_addr = scan_ble(vehicle_id)

            if (kit_ble_addr != None):
                bottom_label("                                   ")
#                 a = datetime.now()
#                 swap_data = open("swap_data.txt","a+")
#                 swap_data.write("%s" %a)
#                 swap_data.write(" Auto is connected\r\n")
#                 swap_data.write("%s" %a)
#                 swap_data.write(" ID is ")
#                 swap_data.write("%s\r\n" %usr_input.get())
                ble_stats.config(text = 'Device found')
                lbl1 = Label(gui,text = "Vehicle Info ").place(x=30,y=250)
                lbl2 = Label(gui,text = "ID                    :").place(x=90,y=280)
                lbl3 = Label(gui,text = "Name              :").place(x=90,y=310)
                lbl4 = Label(gui,text = "Address          :").place(x=90,y=340)
                lbl5 = Label(gui,text = "Energy used   :").place(x=90,y=370)
                lbl4 = Label(gui,text = "Amount(INR)  :").place(x=90,y=400)
                
                #temporary values.
                global energy_used, cost
                energy_used = "2.5" + "KWh"
                cost = "450"
                
                lbl2_val = Label(gui,text = vehicle_id).place(x=200,y=280)
                lbl3_val = Label(gui,text = "RACEnergy_1").place(x=200,y=310)
                lbl4_val = Label(gui,text = kit_ble_addr).place(x=200,y=340)
                lbl5_val = Label(gui,text = energy_used).place(x=200,y=370)
                lbl6_val = Label(gui,text = cost).place(x =200,y=400)
                #writing all the values to swap_data.txt file
#                 a= datetime.now()
#                 swap_data.write("%s" %a)
#                 swap_data.write(" Cost is " + "%s\r\n " %cost)
#                 swap_data.write("%s" %a + " Energy consumed is " + "%s\r\n" %energy_used)
                
                print("Vehicle ID     : ",vehicle_id)
                print("Name           :  RACEnergy_1")
                print("Address        : ",kit_ble_addr)
                
                #Confirm button for entering the batterey collection
                payment_button = Button(gui, text = "Confirm Payment", command = latch_status)
                payment_button.place(x = 180, y = 450)
                
                
            else:
                ble_stats.config(text = 'Vehicle not found!!!')
                print("Vehicle not found!!!")              
    else:
        bottom_label("ID cannot be empty")
        print("ID cannot be empty")
        
def cncl_btn_click(usr_id_entry):
    usr_id_entry.delete(0,END)

def bottom_label(stv):
    id_status = Label(gui, text = stv).place(x=15,y=680)
    

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
