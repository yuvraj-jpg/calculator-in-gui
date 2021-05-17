from tkinter import *

cal=Tk()
cal.title("Calculator")
cal.geometry("380x568")
cal.maxsize(380,568)
cal.minsize(380,568)
cal.configure(background="grey")
#button functioin
def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="error"
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
# for Entry display
scvalue=StringVar()
scvalue.set("")
screen=Entry(cal,textvariable=scvalue,font="timesroman 60 bold")
screen.pack()




# frame and button
f1=Frame(cal)

b=Button(f1,text=".",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f1,text="0",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f1,text="=",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f1,text="0",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button-1>",click)
f1.pack(side="bottom",fill=X)

f1=Frame(cal)

b=Button(f1,text="1",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
b=Button(f1,text="2",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
b=Button(f1,text="3",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
b=Button(f1,text="0",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
f1.pack(side="bottom",fill=X)

b=b=f1=Frame(cal)

b=Button(f1,text="4",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
b=Button(f1,text="5",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
b=Button(f1,text="6",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
b=b=Button(f1,text="*",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)

f1.pack(side="bottom",fill=X)

f1=Frame(cal)

b=Button(f1,text="7",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
b=Button(f1,text="8",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
b=Button(f1,text="9",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
b=Button(f1,text="+",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
f1.pack(side="bottom",fill=X)

f1=Frame(cal)

b=Button(f1,text="-",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
b=Button(f1,text="%",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
b=Button(f1,text="/",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)
b=Button(f1,text="C",padx=40,pady=35)
b.pack(side="left")
b.bind("<Button>",click)

f1.pack(side="bottom",fill=X)


cal.mainloop()