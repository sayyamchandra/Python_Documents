
#sayyam chandra
#code for rolling the dice


import tkinter
from PIL import Image, ImageTk
import random


root = tkinter.Tk()
root.geometry('400x400')
root.title('Dice_Roll')


l0 = tkinter.Label(root, text="")
l0.pack()


l1 = tkinter.Label(root, text="THE PERSON WITH HIGHEST SCORE WILL WIN! MAKE YOUR OWN RULES", fg = "light green",
        bg = "dark green",
        font = "Helvetica 16 bold italic")
l1.pack()


dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

Images_dice = ImageTk.PhotoImage(Image.open(random.choice(dice)))


label1 = tkinter.Label(root, image=Images_dice)
label1.image = Images_dice


label1.pack( expand=True)

# function activated by button
def rolling_dice():
    Images_dice = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=Images_dice)
    # keep a reference
    label1.image = Images_dice



button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)


button.pack( expand=True)


root.mainloop()
