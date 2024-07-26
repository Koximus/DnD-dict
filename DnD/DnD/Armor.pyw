
from tkinter import *
root = Tk()
root.title("Sebzes calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")


def dmg_calc(strin):
    dmg_list = [int(i) for i in strin.split() if i.isdigit()]       # ez a buzi egy listát csinál...
    dmg_int = dmg_list[0]
    if strin.count("armor") > 1:
        clear()

        return "ERROR "




    if "Light armor" in strin:
        dmg_reduction = dmg_int * 0.1
        for i in range(1, dmg_int):
                dmg_int -= 1
                if i >= dmg_reduction or i == 5:
                    break
                if dmg_int == 0:
                    break
                text = ("= " + str(dmg_int))
        return text

    if "Medium armor" in strin:
        dmg_reduction = dmg_int * 0.2
        for i in range(1, dmg_int):
            dmg_int -= 1
            if i >= dmg_reduction or i == 8:
                break
            if dmg_int == 0:
                break

            text = ("= " + str(dmg_int))
        return text

    if "Heavy armor" in strin:
        dmg_reduction = dmg_int * 0.3

        for i in range(1, dmg_int):
            dmg_int -= 1
            if i >= dmg_reduction or i == 12:
                break
            if dmg_int == 0:
                break
        text = ("= " + str(dmg_int))

        return text


dmg = ""


def show(value):
    global dmg
    dmg += value
    label_result.config(text=dmg)


def clear():
    global dmg
    dmg = ""
    label_result.config(text=dmg)


label_result = Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()


Button(root, text="C", width=4, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#3697f5",
       command=lambda: clear()).place(x=10, y=100)
Button(root, text="Light", width=6, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show(" Light armor ")).place(x=120, y=100)
Button(root, text="Medium", width=7, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show(" Medium armor ")).place(x=270, y=100)
Button(root, text="Heavy", width=6, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show(" Heavy armor ")).place(x=430, y=100)

Button(root, text="7", width=4, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=4, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("8")).place(x=120, y=200)
Button(root, text="9", width=4, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("9")).place(x=230, y=200)

Button(root, text="4", width=4, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=4, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("5")).place(x=120, y=300)
Button(root, text="6", width=4, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("6")).place(x=230, y=300)

Button(root, text="1", width=4, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=4, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("2")).place(x=120, y=400)
Button(root, text="3", width=4, height=1, font=("arial", 25, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("3")).place(x=230, y=400)
Button(root, text="0", width=4, height=2, font=("arial", 63, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("0")).place(x=340, y=200)
Button(root, text="Calc", width=12, height=1, font=("arial", 35, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show(dmg_calc(dmg))).place(x=120, y=500)


root.mainloop()
