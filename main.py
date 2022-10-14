import random
from tkinter import *

root = Tk()
root.geometry('900x500')
root.title('Dice Roller')

main_label = Label(text='', font='Arial 300 bold')

def diceroll():
    dices = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    main_label.configure(text=f'{random.choice(dices)}')
    main_label.pack()

Button(text="Roll the dice", command=diceroll).pack()


root.mainloop()