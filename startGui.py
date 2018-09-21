from tkinter import *
import os, sys
import stat

def show(var):
    print(var.get())

def show1(var):
    print(var)    

def createDir(mainWindow):

    mainWindow.destroy()
    createDirWindow = Tk(className=" Create Directory")

    userFrame = Frame(createDirWindow)
    userFrame.pack()

    user = Label(userFrame,text="User Permissions")
    user.pack()

    ur = BooleanVar()
    uw = BooleanVar()
    ux = BooleanVar()
    Checkbutton(userFrame, text = "Read", variable = ur,command=lambda: show(ur)).pack()
    Checkbutton(userFrame, text = "Write", variable = uw).pack()
    Checkbutton(userFrame, text = "Execute", variable = ux).pack()

    groupFrame = Frame(createDirWindow)
    groupFrame.pack()

    group = Label(groupFrame,text="Group Permissions")
    group.pack()

    gr = BooleanVar()
    gw = BooleanVar()
    gx = BooleanVar()
    Checkbutton(groupFrame, text = "Read", variable = gr,command=lambda: show(gr)).pack()
    Checkbutton(groupFrame, text = "Write", variable = gw).pack()
    Checkbutton(groupFrame, text = "Execute", variable = gx).pack()
    
    otherFrame = Frame(createDirWindow)
    otherFrame.pack()

    other = Label(otherFrame,text="Other Permissions")
    other.pack()

    otr = BooleanVar()
    otw = BooleanVar()
    otx = BooleanVar()
    Checkbutton(otherFrame, text = "Read", variable = otr,command=lambda: show(otr)).pack()
    Checkbutton(otherFrame, text = "Write", variable = otw).pack()
    Checkbutton(otherFrame, text = "Execute", variable = otx).pack()

    path = ""
    Entry(createDirWindow,textvariable=path).pack()
    name = ""
    Entry(createDirWindow,textvariable=name).pack()
    fullPath = ""

    fullPath = os.path.join(path,name)
    fp = StringVar()
    fp.set(fullPath)

    Button(createDirWindow, text='Submit', width=25, command=lambda: show1(fp)).pack()
    
    createDirWindow.mainloop()


def chgPer(mainWindow):
    mainWindow.destroy()
    chgPerWindow = Tk(className=" Change Permission")
    chgPerWindow.mainloop()

def main():
    mainWindow = Tk(className=" Permissions")
    createDirButton = Button(mainWindow, text='Create Directory', width=25, command=lambda: createDir(mainWindow))
    createDirButton.pack()
    chgPerButton = Button(mainWindow, text='Change Permission', width=25, command=lambda: chgPer(mainWindow))
    chgPerButton.pack()
    mainWindow.mainloop()

if __name__ == "__main__":
    main()