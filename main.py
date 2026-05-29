# IMPORTS
import tkinter as tk
import settings as s
import os

# WINDOW
WIDTH = 800
HEIGHT = 600
bg="skyblue"
wn = tk.Tk()
wn.geometry(f"{WIDTH}x{HEIGHT}")
wn.iconphoto(False, tk.PhotoImage(file="assets/lilnig.png"))
wn.configure(background=bg)
wn.resizable(False, False)
wn.title("Best game CZ/SK/UA")

# FUNCTIONS
def credits():
    wn.destroy()
    def ok():
        wn2.destroy()
        os.system("python3 main.py")
    wn2=tk.Tk()
    wn2.iconphoto(False, tk.PhotoImage(file="assets/lilnig.png"))
    wn2.geometry(f"{WIDTH}x{HEIGHT}")
    wn2.configure(background=bg)
    wn2.resizable(False, False)
    wn2.title("Best game CZ/SK/UA")
    lblc=tk.Label(wn2, text="CREDITS\nGraphics: Karel Mracek\nProgramming: Ondrej Selucky\nFinger: jew\nHotel: Trivago\nERIK HANYS: TESTOSTERON++", font=("Arial", 20), background=bg)
    lblc.place(x=WIDTH/5, y=100)
    okbtn = tk.Button(wn2, text="OK", font=("Arial", 40), width=9,command=ok,background="cyan")
    okbtn.place(x=WIDTH/5, y=500)

def new_game():
    wn.destroy()
    os.system("python3 game.py")

# MAIN STUFF
lbl = tk.Label(wn, text="nicolas tovt: the game", font=("Arial", 40), background=bg)
lbl.place(x=WIDTH/5, y=100)

btn1 = tk.Button(wn, text = "New Game", font=("Arial", 40), width=9,command=new_game,background="cyan")
btn1.place(x=WIDTH/5, y=200)

btn2 = tk.Button(wn, text = "Load Game", font=("Arial", 40), width=9,state="disabled",background="cyan")
btn2.place(x=WIDTH/5, y=280)

btn3 = tk.Button(wn, text = "Credits", font=("Arial", 40), width=9,command=credits,background="cyan")
btn3.place(x=WIDTH/5, y=360)

btn4 = tk.Button(wn, text = "Exit", font=("Arial", 40), width=9,command=wn.destroy,background="cyan")
btn4.place(x=WIDTH/5, y=440)

# MAIN LOOP
wn.mainloop()