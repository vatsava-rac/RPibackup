# Required python modules..
import os
import sys
from tkinter import *
from bluepy.btle import *
from functools import partial
from datetime import datetime, date
import binascii
from bluepy import btle


gui = Tk()
gui.configure(bg = '#dbe1e4')

# String declarations
usr_inpt = StringVar()
vehicle_id   = StringVar()
kit_ble_addr = StringVar()

## Container of all the tkinter elements.
# @note Beginning of the code.
def home():
     
    width = gui.winfo_screenwidth()
    width_1 = str(width)
    print(width_1)
    height = gui.winfo_screenheight()
    height_1 = str(height)
    print(height_1)
    gui.geometry(width_1 + "x" + height_1+"0"+"0")

    # Title for the GUI page
    gui.title("RACEnergy BSS")
    
    title_lbl = Label(gui, text = "RACENERGY BATTERY SWAPPING STATION", font = ('Futura BK BT', 30), bg = '#dbe1e4').place(x = 0.220 * width, y = 0.056 * height)

    #Create label
    usr_lbl_x = 0.350 * width
    usr_lbl_y = 0.20 * height
    usr_id_lbl = Label(gui,text = "VEHICLE NUMBER", font = ('Futura BK BT', 15), bg = '#dbe1e4').place(x = usr_lbl_x, y = usr_lbl_y)

    #Create entry box to enter the auto number
    usr_entry_x = 0.49 * width
    usr_entry_y = 0.20 * height
    usr_id_entry = Entry(gui,textvariable = usr_inpt, width = 30, cursor = 'arrow').place(x = usr_entry_x, y = usr_entry_y)
    #usr_id_entry.place(x = 580, y = 50)

   ## Showing the Kit status
   # Status can be IDLE, VEHICLE FOUND, VEHICLE NOT FOUND, SCANNING
    status_lbl_x = 0.06 * width
    status_lbl_y = 0.28 * height
    status_lbl = Label(gui,text = "Kit status :", font = (20), bg = '#dbe1e4').place(x = status_lbl_x,y = status_lbl_y)
    ble_stats("IDLE")

    cnf_fun = partial(cnf_btn_click,usr_inpt)
    #create CONFIRM button
    cnfm_btn_x = 0.40 * width
    cnfm_btn_y = 0.28 * height
    cnfm_btn = Button(gui,text = "CONFIRM",command = cnf_fun, activebackground = "dodger blue", activeforeground = "black", font =('Futura BK BT',14),
                      bg = '#dbe1e4')
    cnfm_btn.place(x = cnfm_btn_x, y = cnfm_btn_y)
    
    cncl_fun = partial(cncl_btn_click,usr_id_entry)

    # Create CANCEL button
    cncl_btn_x = 0.52 * width
    cncl_btn_y = 0.28 * height
    cncl_btn = Button(gui,text = "CANCEL", command = cncl_fun, activebackground = "dodger blue", activeforeground = "black", font = ('Futura BK BT',14),
                      bg = '#dbe1e4')
    cncl_btn.place(x = cncl_btn_x, y = cncl_btn_y)

    # Create RESET button
    rst_btn = Button(gui,text = "RESET", command = restart_app, activebackground = "pink", activeforeground = "red")
    rst_btn.pack(side = BOTTOM)

## Command for the RESET button
# Restarts the GUI process from the beginning.
def restart_app():
    python = sys.executable
    os.execl(python,python, *sys.argv)
    
def timeout():
    width = gui.winfo_screenwidth()
    height = gui.winfo_screenheight()
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("  %H:%M:%S")
    current_date = today.strftime("%d/%m/20%y")
    time_lbl = Label(gui, text = current_date + current_time, font = ('Futura BK BT' ,12), bg = '#dbe1e4').place(x = 0.87 * width, y = 0.01 * height)
    gui.after(500, timeout)

## Gives the status of the Auto Latch
# Status is shown after the Confirm Button is pressed. 
# Data should be given here after the verification of the old batteries is completed...
# New batteries data is sent to conversion kit via BLE here. 
def latch_status(bb):
    # Sending command to open latch of auto
    width = gui.winfo_screenwidth()
    height = gui.winfo_screenheight()
    
    write_to_characteristic("52454b53303030303030303030303034", "52454b43533034303030303030303031", "OPEN LATCH", bb)
    print("Auto latch is open")
    auto_latch_stats = Label(gui,text = "Auto latch is open", font = (15), bg = '#dbe1e4').place(x = 0.45 * width, y = 0.74 * height)
    bss_latch_stats = Label(gui, text = "BSS latch is open", font = (15), bg = '#dbe1e4').place(x = 0.45 * width, y = 0.77 * height)

    # Read old Battery pack ID's 
    old_packs = read_characteristic("52454b53303030303030303030303035", "52454b43533035303030303030303032", bb).decode()
    old_packs = bytes.fromhex(old_packs).decode('utf-8')
    print(old_packs)

    # here the doors of the empty BSS slots are opened.
    # incoming from the internal process
    c = "Batteries verified"
        
    if c == "Batteries verified":
        # Sending new Battery pack ID's
        write_to_characteristic("52454b53303030303030303030303035", "52454b43533035303030303030303031", "RACEA03A001", bb)
        write_to_characteristic("52454b53303030303030303030303035", "52454b43533035303030303030303031", "RACEA03A002", bb)
        write_to_characteristic("52454b53303030303030303030303035", "52454b43533035303030303030303031", "RACEA03A003", bb)
        write_to_characteristic("52454b53303030303030303030303035", "52454b43533035303030303030303031", "RACEA03A004", bb)
            
        # reading the status of the latch of auto
        latchStatus = read_characteristic("52454b53303030303030303030303034", "52454b43533034303030303030303032", bb).decode()
        wait_for_latchdata(latchStatus)
        latch_status1(latchStatus)
        
        end_swap = Button(gui, text = "END SWAP", command = close_swap_file, font =(16)).place(x = 0.50 * width, y = 0.68 * height)
        bb.disconnect()
    else:
        # What should be done here....
        print("Batteries are not matching")

## Command for END SWAP button.
## can read the latch status and update the latch status label...
def close_swap_file():
    
    print("Auto released")
    time.sleep(5)
    restart_app()


## Scans for the Bluetooth address of the device. 
def scan_ble(uid):
    scanner = Scanner()
    devices = scanner.scan(3.0)
    for dev in devices:
        for (adtype, desc, value) in dev.getScanData():
            if("Complete Local Name" == desc):
                if(uid == value):
                    return dev.addr
                else:
                    return None

## Function to establish connection with entered UID
# @param local_name Local name entered by the user
# uid is specific to each module
# @returns Status of connection
def establish_connection(local_name):
    scanner = Scanner()
    devices = scanner.scan(3.0) # scan for 3 seconds
    #ble_stats.config(text = "Scanning...")

    for dev in devices:
        for (adtype, desc, value) in dev.getScanData():
            #print("available address are")
            #print(dev.addr)
            if("Complete Local Name" == desc):
                print("here1")
                if(local_name == value):
                    print("connection initiated")
                    per = btle.Peripheral()
                    per.connect(dev.addr, "random")
                    per.setSecurityLevel(level="high")
                    print("addr is " + dev.addr)
                    statusOfConnection = per.getState() 
                    print(statusOfConnection)
                    #print(per)
                    return(statusOfConnection, per)
                else:
                    print("No device found")
                    statusOfConnection = per.getState() 
                    print(statusOfConnection)
                    return(statusOfConnection)

## Scans for the available services
def services_available():
    print ("available services...")
    for svc in per.services:
        print (svc)

## Read data from specific characteristics
# @param servID service UUID for the characteristic
# @param charaID characteristic UUID
# @returns Returns the value from the characteristic
# @note If UUID is in hex format enter it normally. If is in 128 bit format, enter it as string.
def read_characteristic(servID, charaID, para):
    
    serviceID = btle.UUID(servID)# to get the UUID in proper format for service
    serv = para.getServiceByUUID(serviceID)# get the service

    characteristicID = btle.UUID(charaID)# get characteristic ID in proper format
    chara = serv.getCharacteristics(characteristicID)[0] #get the characteristic
    chara_value = chara.read()
    chara_value_decoded = (chara_value.decode())
    return(binascii.b2a_hex(chara_value))

## Write data to specific characteristic
# @param servID Service UUID for the characteristic
# @param charaID Characteristic UUID
# @param data Data to be written into the characteristic. Data should be in string format.
# @note If UUID is in hex format enter it normally. If is in 128 bit format, enter it as string.
def write_to_characteristic(servID, charaID, data, para):
    serviceID = btle.UUID(servID)# to get the UUID in proper format for service
    serv = para.getServiceByUUID(serviceID)# get the service

    characteristicID = btle.UUID(charaID)# get characteristic ID in proper format
    chara = serv.getCharacteristics(characteristicID)[0] #get the characteristic
    encoded = (data.encode())# data should be sent in bytes format
    chara_value = chara.write(encoded)

## Waits for the latch data
# Waits until the latch data is arraived
# @param latchdata Give the decoded latch status
# @returns Latchdata
def wait_for_latchdata(latchdata):
    if len(latchdata) > 1:
        latchdata = bytes.fromhex(latchdata).decode('utf-8')
        return(latchdata)
    else:
        time.sleep(0.7)
        print("waiting for the latch data")
        wait_for_latchdata(latchdata)

## Function to make sure latch is closed
# @param latchdata Takes latchdata as argument
def latch_status1(latchdata):
    data = bytes.fromhex(latchdata).decode('utf-8')
    
    if data == "Latch is closed":
        print(data)
        return(latchdata)
    else:
        print("Close the auto latch")
        time.sleep(2)
        latch_status(latchdata)

## Commands for the CONFIRM button
# @note It is pressed after the auto driver enters his Auto number
# @param usr_input Text entered by the Auto
# @param ble_stats Bluetooth ID scanned by BLE. 
def cnf_btn_click(usr_input):
    
    width = gui.winfo_screenwidth()
    height = gui.winfo_screenheight()
    
    testData = "123"
    global vehicle_id
    vehicle_id = usr_input.get() # Value is getting from the entry box.
    print(vehicle_id)

    if (vehicle_id != ""): #When vehicle ID is not entered and CONFIRM is clicked

        if (len(vehicle_id) != 10): # All the vehicle ID's are assumed to be 10 characters length.
            print("Invalid ID")
            bottom_label("Invalid ID                ") # bottom label will tell about the entered vehicle ID. 
#             time.sleep(3)
#             bottom_label("")
        else:
            bottom_label("                                   ")
            ble_stats("Searching for your Auto")
            time.sleep(1)
            kit_ble_addr = scan_ble(vehicle_id) # gives the bluetooth address to the device
            a, b = establish_connection(vehicle_id)
            print("Decives are connected before authentication.")
            # connection is established now. 
            
            if (kit_ble_addr != None):

                # entering into the log file
                # entered data is about vehicle ID. 
                d = datetime.now()
                e = d 
                log_data = open("log_data.txt","a+")
                log_data.write("%s" %e)
                log_data.write(" Auto is connected, verification should be done.\r\n")
                log_data.write("%s" %e)
                log_data.write(" ID is ")
                log_data.write("%s\r\n" %usr_input.get())
                log_data.close()

                # authentication here...
                if a == "conn":
                    # Verification of connection
                    # Later authertication on both sides should happen....
                    
                    received_value = (read_characteristic("52454b53303030303030303030303031", "52454b43533031303030303030303031", b))
                    write_to_characteristic("52454b53303030303030303030303031", "52454b43533031303030303030303032", testData, b)
                    received_check = received_value.decode()
                    print("verification data received from conversion kit is")
                    print(received_check)

                    if received_check == "2235":
                        ble_stats('Auto found                       ')
                        time.sleep(2)
                        ## Reading billing info
                        # SoC and Battery ID's are read to Raspberry pi
                        d = datetime.now()
                        log_data = open("log_data.txt","a+")
                        log_data.write("%s" %d)
                        log_data.write(" Verification data is exchanged. Auto is connected and paired.\r\n")
                        log_data.close()
                        
                        soc = read_characteristic("52454b53303030303030303030303032", "52454b43533032303030303030303032", b).decode()
                        print("device soc is " + soc)
                        BatteryID = read_characteristic("52454b53303030303030303030303032", "52454b43533032303030303030303031", b).decode()
                        BatteryID = bytes.fromhex(BatteryID).decode('utf-8')
                        print("Arriving batteries are " + BatteryID)

                        ## Kit status service
                        # Alert status and Tamper sensor outputs are read to Raspberry pi
                        alert_status = read_characteristic("52454b53303030303030303030303033", "52454b43533033303030303030303031", b).decode()
                        alert_status = bytes.fromhex(alert_status).decode('utf-8')
                        print("alert status is " + alert_status)
                        tamper_sensor = read_characteristic("52454b53303030303030303030303033", "52454b43533033303030303030303032", b).decode()
                        print(tamper_sensor)

                        # Creating th elabels which are to be shown to auto driver.
                        lbl1_x = 0.35 * width
                        lbl1_y = 0.37 * height
                        lbl1 = Label(gui,text = "Vehicle Info ", font = (20), bg = '#dbe1e4').place(x = lbl1_x, y = lbl1_y)
                        lbl2 = Label(gui,text = "ID                    :", font = (16), bg = '#dbe1e4').place(x = 0.41 * width, y = 0.40 * height)
                        lbl3 = Label(gui,text = "Name              :", font = (16), bg = '#dbe1e4').place(x = 0.41 * width, y = 0.45 * height)
                        lbl4 = Label(gui,text = "Address           :", font = (16), bg = '#dbe1e4').place(x = 0.41 * width, y = 0.50 * height)
                        lbl5 = Label(gui,text = "Energy used    :", font = (16), bg = '#dbe1e4').place(x = 0.41 * width, y = 0.55 * height)
                        lbl4 = Label(gui,text = "Amount(INR)   :", font = (16), bg = '#dbe1e4').place(x = 0.41 * width, y = 0.60 * height)

                        #temporary values.
                        global energy_used, cost
                        energy_used = "2.5" + "KWh"
                        cost = "450"

                        lbl2_val = Label(gui,text = vehicle_id, font = (16), bg = '#dbe1e4').place(x = 0.55 * width,y = 0.40 * height)
                        lbl3_val = Label(gui,text = "RACEnergy_1", font = (16), bg = '#dbe1e4').place(x = 0.55 * width, y = 0.45 * height)
                        lbl4_val = Label(gui,text = kit_ble_addr, font = (16), bg = '#dbe1e4').place(x = 0.55 * width, y = 0.50 * height)
                        lbl5_val = Label(gui,text = energy_used, font = (16), bg = '#dbe1e4').place(x = 0.55 * width, y = 0.55  * height)
                        lbl6_val = Label(gui,text = cost, font = (16), bg = '#dbe1e4').place(x = 0.55 * width, y = 0.60 * height)

                        #writing all the values to swap_data.txt file
                        d = datetime.now()
                        swap_data = open("swap_data.txt","a+")
                        swap_data.write("%s" %d)
                        swap_data.write(" Cost is " + "%s\r\n " %cost)
                        swap_data.write("%s" %d + " Energy consumed is " + "%s\r\n" %energy_used)
                        swap_data.close()

                        print("Vehicle ID     : ",vehicle_id)
                        print("Name           :  RACEnergy_1")
                        print("Address        : ",kit_ble_addr)

                        #Confirm button for entering the batterey collection
                        latch_fun = partial(latch_status, b)
                        payment_button = Button(gui, text = "CONFIRM PAYMENT", command = latch_fun, font = (16), bg = '#dbe1e4')
                        payment_button.place(x = 0.35 * width, y = 0.68 * height)
                    else:
                        # What should be done here....
                        print("Batteries are not matching")
                else:
                    print("Invalid device")
                    b.disconnect()                

            else:
                ble_stats('Vehicle not found!!!')
                print("Vehicle not found!!!")              
    else:
        bottom_label("ID cannot be empty")
        print("ID cannot be empty")


def cncl_btn_click(usr_id_entry):
    usr_id_entry.delete(0,END)

def bottom_label(stv):
    width = gui.winfo_screenwidth()
    height = gui.winfo_screenheight()
    id_status = Label(gui, text = stv, font = (16), bg = '#dbe1e4').place(x = 0.7 * width, y = 0.20 * height)

def ble_stats(ble_status):
    width = gui.winfo_screenwidth()
    height = gui.winfo_screenheight()
    Label(gui, text = ble_status, font = (16), bg = '#dbe1e4').place(x = 0.125 * width, y = 0.28 * height)

home()
timeout()
gui.mainloop()


