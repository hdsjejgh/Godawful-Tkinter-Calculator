from tkinter import PhotoImage, Label, Button,Tk

def dele():
    if not (" " in ans.cget("text")):
        ans.config(text=ans.cget("text")[0:len(ans.cget("text"))-1])
    else:
        ans.config(text="")
def add(event):
    if " " in ans.cget("text"):
        clear()
    ans.config(text=ans.cget("text")+event.widget.cget("text"))
def clear():
    ans.config(text="")
def solve():
    try:
        solved=str(eval(ans.cget("text")))
        if len(solved)>15 and "."in solved:
            if "." in solved[0:15]:
                solved=solved[0:15]

    except SyntaxError:
        solved="Syntax Error"
        error=True
    except ZeroDivisionError:
        solved="Cannot Do /0"
        error=True
    finally:
        ans.config(text=solved)


w = Tk()
w.geometry("130x250")
w.title("calculator")
w.config(background="LightGray")
w.resizable(0,0)
icong = PhotoImage(file='CalcWin7.png')
w.iconphoto(True,icong)
w.rowconfigure(0, minsize=125/3)
ans = Label(w, text="",font=("Courier", 10, 'bold'),fg='Black',bg="LightGray",justify='left',pady=0)
ans.place(x=0,y=10)
button1 = Button(w,text="1",relief="raised",bd=10,width=0)
button2 = Button(w,text="2",relief="raised",bd=10,width=0)
button3 = Button(w,text="3",relief="raised",bd=10,width=0)
button4 = Button(w,text="4",relief="raised",bd=10,width=0)
button5 = Button(w,text="5",relief="raised",bd=10,width=0)
button6 = Button(w,text="6",relief="raised",bd=10,width=0)
button7 = Button(w,text="7",relief="raised",bd=10,width=0)
button8 = Button(w,text="8",relief="raised",bd=10,width=0)
button9 = Button(w,text="9",relief="raised",bd=10,width=0)
button0 = Button(w,text="0",relief="raised",bd=10,width=0)
buttona = Button(w,text="+",relief="raised",bd=10,width=0)
buttons = Button(w,text="-",relief="raised",bd=10,width=0)
buttonm = Button(w,text="*",relief="raised",bd=10,width=0)
buttond = Button(w,text="/",relief="raised",bd=10,width=0)
buttone = Button(w,text="=",relief="raised",bd=10,width=0,command=solve)
buttonp = Button(w,text=".",relief="raised",bd=10,width=0)
buttoncl = Button(w,text="C",relief="raised",bd=10,width=0,command=clear)
buttonde = Button(w,text="D",relief="raised",bd=10,width=0,command=dele)
buttonop = Button(w,text="(",relief="raised",bd=10,width=0)
buttoncp = Button(w,text=")",relief="raised",bd=10,width=0)
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
buttonp.grid(row=4,column=0)
button0.grid(row=4,column=1)
buttona.grid(row=1,column=3)
buttons.grid(row=2,column=3)
buttonm.grid(row=3,column=3)
buttond.grid(row=4,column=3)
buttone.grid(row=4,column=2)
buttoncl.grid(row=5,column=3)
buttonop.grid(row=5,column=0)
buttoncp.grid(row=5,column=1)
buttonde.grid(row=5,column=2)

button1.bind('<Button-1>',add)
button2.bind('<Button-1>',add)
button3.bind('<Button-1>',add)
button4.bind('<Button-1>',add)
button5.bind('<Button-1>',add)
button6.bind('<Button-1>',add)
button7.bind('<Button-1>',add)
button8.bind('<Button-1>',add)
button9.bind('<Button-1>',add)
button0.bind('<Button-1>',add)
buttonp.bind('<Button-1>',add)
buttona.bind('<Button-1>',add)
buttons.bind('<Button-1>',add)
buttonm.bind('<Button-1>',add)
buttond.bind('<Button-1>',add)
buttonop.bind('<Button-1>',add)
buttoncp.bind('<Button-1>',add)

w.mainloop()
