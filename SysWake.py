# Imports needed modules :)
from tkinter import *
import wakeonlan as wol
import time as time

# Arrays are set as blank
NameSlots = []
IPSlot = []
MACSlot = []
SellSlot = []
PORTSlot = []
GROUPSlot = []
ShutdownSlot = []
currentSlot = 0
levelCheck = 0

# Adds config files if non-existent if they exist nothing happens
save = open('name_Config.txt', 'a')
saveIP = open('IP_Config.txt', 'a')
saveMAC = open('MAC_Config.txt', 'a')
savePORT = open('PORT_Config.txt', 'a')
saveGROUP = open('GROUP_Config.txt', 'a')
saveSettings = open('Settings_Config.txt', 'a')
save.close()
saveIP.close()
saveMAC.close()
savePORT.close()
saveGROUP.close()
saveSettings.close()

# HEB CORP Print
print("██╗░░██╗███████╗██████╗░  ░█████╗░░█████╗░██████╗░██████╗░")
print("██║░░██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
print("███████║█████╗░░██████╦╝  ██║░░╚═╝██║░░██║██████╔╝██████╔╝")
print("██╔══██║██╔══╝░░██╔══██╗  ██║░░██╗██║░░██║██╔══██╗██╔═══╝░")
print("██║░░██║███████╗██████╦╝  ╚█████╔╝╚█████╔╝██║░░██║██║░░░░░")
print("╚═╝░░╚═╝╚══════╝╚═════╝░  ░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░")
print("Thank you for using our official code")

# Initializes the window itself with size and changeability
window = Tk()
window.geometry('725x571')
window.title('SysWake')
window.resizable(False, False)

# Scrollbar Creation
main_frame = Frame(window)
main_frame.place(x=0, y=44, width=600, height=527)
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=YES)
my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
second_frame = Frame(my_canvas)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Prints the column labels to the screen
Name = Label(window, text="Friendly PC Name")
Name.place(x=0, y=23)
IP = Label(window, text="IP Address")
IP.place(x=217, y=23)
MAC = Label(window, text="MAC Address")
MAC.place(x=320, y=23)
PORT = Label(window, text="Port")
PORT.place(x=187, y=23)
GROUP = Label(window, text="Select")
GROUP.place(x=450, y=23)
GROUP = Label(window, text="Group")
GROUP.place(x=510, y=23)


def wakePC():
    global currentSlot
    currentSlotHold = currentSlot
    while currentSlotHold != 0:
        if str(SellSlot[currentSlotHold-1].get()) == "yes":
            print(str(MACSlot[currentSlotHold - 1].get()))
            wol.send_magic_packet(str(MACSlot[currentSlotHold - 1].get()),
                                  ip_address=str(IPSlot[currentSlotHold - 1].get()),
                                  port=int(PORTSlot[currentSlotHold - 1].get()))
            print("Woke", str(NameSlots[currentSlotHold - 1].get()))
            time.sleep(int(Wait.get()))
        currentSlotHold -= 1


def group_Wake():
    # Group Wake Window Init
    GroupWake = Tk()
    GroupWake.geometry('250x130')
    GroupWake.title('GroupWake')
    GroupWake.resizable(False, False)

    # wake Group Function
    def wakeGroup():
        global currentSlot
        currentSlotHold = currentSlot
        while currentSlotHold != 0:
            if str(GROUPSlot[currentSlotHold - 1].get()) == str(GroupSelection.get()):
                wol.send_magic_packet(str(MACSlot[currentSlotHold - 1].get()),
                                      ip_address=str(IPSlot[currentSlotHold - 1].get()),
                                      port=int(PORTSlot[currentSlotHold - 1].get()))
                print("Woke", str(NameSlots[currentSlotHold - 1].get()))
                time.sleep(int(Wait.get()))

            elif str(GroupSelection.get()) == "All":
                wol.send_magic_packet(str(MACSlot[currentSlotHold - 1].get()),
                                      ip_address=str(IPSlot[currentSlotHold - 1].get()),
                                      port=int(PORTSlot[currentSlotHold - 1].get()))
                print("Woke", str(NameSlots[currentSlotHold - 1].get()))
                time.sleep(int(Wait.get()))
            currentSlotHold -= 1

    # Drawing User Interface
    GroupSelection = Entry(GroupWake, bd=2, width=10)
    GroupSelection.place(x=95, y=0)
    InfoLabel = Label(GroupWake, text="Group to Wake")
    InfoLabel.place(x=85, y=26)
    MoreInfoLabel1 = Label(GroupWake, text="Uses delay on main page")
    MoreInfoLabel2 = Label(GroupWake, text="This might take longer than a single Wake")
    MoreInfoLabel1.place(x=57, y=78)
    MoreInfoLabel2.place(x=13, y=104)

    GroupWakeButton = Button(GroupWake, text="Wake PCs With that Group", command=lambda: wakeGroup())
    GroupWakeButton.place(x=52, y=52)

    GroupWake.mainloop()


# Updates the scroll region for the dynamic bar
def updateScrollRegion():
    global my_canvas
    my_canvas.update_idletasks()
    my_canvas.config(scrollregion=my_canvas.bbox("all"))


# Adds a new row to the bottom of the list
def add_new():
    global currentSlot
    # Adds the new entry to the loaded arrays (These store the data for which entry is which)
    PORTSlot.append(str(currentSlot))
    NameSlots.append(str(currentSlot))
    IPSlot.append(str(currentSlot))
    SellSlot.append(str(currentSlot))
    MACSlot.append(str(currentSlot))
    GROUPSlot.append(str(currentSlot))
    row = currentSlot + 1
    # Place the entries on screen
    NameSlots[currentSlot] = Entry(second_frame, bd=2, width=30)
    NameSlots[currentSlot].grid(column=0, row=row)

    IPSlot[currentSlot] = Entry(second_frame, bd=2, width=16)
    IPSlot[currentSlot].grid(column=2, row=row)

    MACSlot[currentSlot] = Entry(second_frame, bd=2, width=20)
    MACSlot[currentSlot].grid(column=3, row=row)

    SellSlot[currentSlot] = Entry(second_frame, bd=2, width=10)
    SellSlot[currentSlot].grid(column=4, row=row)

    PORTSlot[currentSlot] = Entry(second_frame, bd=2, width=4)
    PORTSlot[currentSlot].grid(column=1, row=row)

    GROUPSlot[currentSlot] = Entry(second_frame, bd=2, width=10)
    GROUPSlot[currentSlot].grid(column=5, row=row)

    currentSlot += 1
    updateScrollRegion()
    return currentSlot


# Removes the single bottom row
def remove_box():
    global currentSlot
    # Deletes the bottom (most recently added) row of entries
    if currentSlot > 0:
        currentSlot -= 1
        NameSlots[currentSlot].destroy()
        NameSlots.pop()

        IPSlot[currentSlot].destroy()
        IPSlot.pop()

        MACSlot[currentSlot].destroy()
        MACSlot.pop()

        SellSlot[currentSlot].destroy()
        SellSlot.pop()

        PORTSlot[currentSlot].destroy()
        PORTSlot.pop()

        GROUPSlot[currentSlot].destroy()
        GROUPSlot.pop()

        updateScrollRegion()
        return currentSlot


# Saves the entries for each row
def saveConf():
    global currentSlot
    currentSlotHold = currentSlot
    currentSlotSave = 0
    # This clears the config files ready to be written
    save = open('name_Config.txt', 'w')
    save.write("")
    save.close()
    saveIP = open('IP_Config.txt', 'w')
    saveIP.write("")
    saveIP.close()
    saveMAC = open('MAC_Config.txt', 'w')
    saveMAC.write("")
    saveMAC.close()
    savePORT = open('PORT_Config.txt', 'w')
    savePORT.write("")
    savePORT.close()
    saveGROUP = open('GROUP_Config.txt', 'w')
    saveGROUP.write("")
    saveGROUP.close()
    saveSettings = open('Settings_Config.txt', 'w')
    saveSettings.write("")
    saveSettings.close()
    save = open('name_Config.txt', 'a')
    saveIP = open('IP_Config.txt', 'a')
    saveMAC = open('MAC_Config.txt', 'a')
    savePORT = open('PORT_Config.txt', 'a')
    saveGROUP = open('GROUP_Config.txt', 'a')
    saveSettings = open('Settings_Config.txt', 'a')
    # This actually writes the entries to the configs
    while currentSlot >= 0:
        if currentSlotSave <= currentSlotHold - 1:
            save.write(NameSlots[currentSlotSave].get() + '\n')
            saveIP.write(IPSlot[currentSlotSave].get() + '\n')
            saveMAC.write(MACSlot[currentSlotSave].get() + '\n')
            savePORT.write(PORTSlot[currentSlotSave].get() + '\n')
            saveGROUP.write(GROUPSlot[currentSlotSave].get() + '\n')
            currentSlotSave += 1
        currentSlot -= 1
    currentSlot = currentSlotHold
    saveSettings.write(Wait.get() + '\n')
    save.close()
    saveIP.close()
    saveMAC.close()
    savePORT.close()
    saveGROUP.close()
    saveSettings.close()


# Loading the entries from file
def loadConf():
    global currentSlot
    # Opens each file for reading as well as getting how many lines (entries) there are
    save = open('name_Config.txt', 'r')
    saveIP = open('IP_Config.txt', 'r')
    saveMAC = open('MAC_Config.txt', 'r')
    savePORT = open('PORT_Config.txt', 'r')
    saveGROUP = open('GROUP_Config.txt', 'r')
    saveSettings = open('Settings_Config.txt', 'r')
    lineCount = len(open('name_Config.txt').readlines())
    lineHold = lineCount
    # Writes them to the screen by adding an entry for the amount of lines then populating them
    if lineCount > 0:
        saveContents = save.readlines()
        IPContents = saveIP.readlines()
        MACContents = saveMAC.readlines()
        PORTContents = savePORT.readlines()
        GROUPContents = saveGROUP.readlines()
        SettingsContents = saveSettings.readlines()
        currentSlotHold = currentSlot
        while lineCount > currentSlot:
            add_new()
            currentSlotHold = currentSlot
        currentSlot = lineCount

        while lineCount >= 0:
            if currentSlot > 0:
                currentSlot -= 1
            NameSlots[currentSlot].delete(0, 'end')
            NameSlots[currentSlot].insert(0, saveContents[currentSlot].replace('\n', ""))
            lineCount -= 1
        lineCount = lineHold
        currentSlot = lineCount

        while lineCount >= 0:
            if currentSlot > 0:
                currentSlot -= 1
            IPSlot[currentSlot].delete(0, 'end')
            IPSlot[currentSlot].insert(0, IPContents[currentSlot].replace('\n', ""))
            lineCount -= 1
        lineCount = lineHold
        currentSlot = lineCount

        while lineCount >= 0:
            if currentSlot > 0:
                currentSlot -= 1
            PORTSlot[currentSlot].delete(0, 'end')
            PORTSlot[currentSlot].insert(0, PORTContents[currentSlot].replace('\n', ""))
            lineCount -= 1
        lineCount = lineHold
        currentSlot = lineCount

        while lineCount >= 0:
            if currentSlot > 0:
                currentSlot -= 1
            GROUPSlot[currentSlot].delete(0, 'end')
            GROUPSlot[currentSlot].insert(0, GROUPContents[currentSlot].replace('\n', ""))
            lineCount -= 1
        lineCount = lineHold
        currentSlot = lineCount

        # Settings
        Wait.delete(0, 'end')
        Wait.insert(0, SettingsContents[0].replace('\n', ""))

        while lineCount >= 0:
            if currentSlot > 0:
                currentSlot -= 1
            MACSlot[currentSlot].delete(0, 'end')
            MACSlot[currentSlot].insert(0, MACContents[currentSlot].replace('\n', ""))
            lineCount -= 1
        currentSlot = currentSlotHold


# Misc 2 for side buttons and top bar
loadButt = Button(window, text='Load Entries from File', command=lambda: loadConf())
loadButt.place(y=92, x=600)
saveButt = Button(window, text='Save Entries to File', command=lambda: saveConf())
saveButt.place(y=118, x=600)
addNew = Button(window, text="Add Row", command=lambda: (add_new()))
addNew.place(y=40, x=600)
removeBox = Button(window, text="Remove Row", command=lambda: (remove_box()))
removeBox.place(y=66, x=600)
Wake = Button(window, text="Wake Selected PCs", command=lambda: (wakePC()))
Wake.grid(column=0, row=0)
Group = Button(window, text="Group Wake", command=lambda: (group_Wake()))
Group.grid(column=1, row=0)
Wait = Entry(window, bd=2, width=10)
Wait.grid(column=2, row=0)
WaitLabel = Label(window, text="Wake Delay (Seconds)")
WaitLabel.grid(column=3, row=0)
loadConf()

# Closes main loop for window
window.mainloop()

# Congrats this is the end :))
