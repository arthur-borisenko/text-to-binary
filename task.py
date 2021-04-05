import tkinter as gui

def diving(__x, __y):
    return __x % __y == 0


def toBinary(x):
    string = ""
    ends = [1, 0]
    s1 = "1"
    s0 = "0"
    while True:
        if diving(x, 2):
            string = string + s0
        else:
            string = string + s1
        x = x // 2
        if x in ends:
            string = string + str(x)
            break
    return string


def reverseStr(string: str):
    strList = list(string)
    rstring = ""
    strList.reverse()
    for letter in strList:
        rstring = rstring + letter
    return rstring


def ubinary(t: str):
    rstring = ""
    for letter in list(t):
        rstring = rstring + " " + reverseStr(toBinary(ord(letter)))
    return rstring
gui2 = gui.Tk()
mainmenu = gui.Menu(gui2)
filemenu = gui.Menu(mainmenu, tearoff=0)
pmenu = gui.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Personalization", menu=pmenu)
mainmenu.add_cascade(label="File", menu=filemenu)
colormenu = gui.Menu(pmenu)
pmenu.add_cascade(label="color", menu=colormenu)
Label = gui.Label(gui2, text="enter string(a-z,A-Z,1-9,!,@,#,$,%,^,&,*,(,),_,+,=", bg="white")
gui2["bg"]="white"

def bgcolor(sel_color):
    Label["bg"]=sel_color
    gui2["bg"] = sel_color

def save(Entry1,text):
    import tkinter.filedialog as saver
    fp=saver.asksaveasfilename(title="save as")
    import os
    if not os.path.exists(fp):
        open(fp,"x")
    else:
        import tkinter.messagebox as mbox
        if mbox.askyesno("replace",f"{fp} already exists.Replace?")==0:
            os.remove(fp)
            open(fp, "x")
    if os.path.exists(fp):
        f=open(fp,"w")
        f.write(f'{Entry1.get()} {text}')

def savebin(Entry1,text):
    import tkinter.filedialog as saver
    fp=saver.asksaveasfilename(title="save as")
    import os
    if not os.path.exists(fp):
        open(fp,"x")
    else:
        import tkinter.messagebox as mbox
        if mbox.askyesno("replace",f"{fp} already exists.Replace?")==0:
            os.remove(fp)
            open(fp, "x")
    if os.path.exists(fp):
        f=open(fp,"w")
        f.write(f'{ubinary(Entry1.get())}')


colormenu.add_command(label="yellow background", command=lambda c="yellow": bgcolor(c))
colormenu.add_command(label="white background", command=lambda c="white": bgcolor(c))
colormenu.add_command(label="green background", command=lambda c="green": bgcolor(c))
colormenu.add_command(label="orange background", command=lambda c="orange": bgcolor(c))
colormenu.add_command(label="pink background", command=lambda c="pink": bgcolor(c))
Entry = gui.Entry(gui2)

Label.pack()
result = gui.Label(gui2, bg="gray")
Entry.pack()
gui2.config(menu=mainmenu)
filemenu.add_command(label="save as", command=lambda c="",e=Entry: save(e,c))
filemenu.add_command(label="save binary", command=lambda c="",e=Entry: savebin(e,c))



# x = input("enter number to convert: ")
# print(abinary(x))
def check(e):
    global result, Entry
    output = ubinary(Entry.get())
    result["text"] = output
    result.pack()


gui2.bind_all("<Return>", check)
gui2.mainloop()
