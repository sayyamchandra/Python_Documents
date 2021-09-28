from tkinter import *


root = Tk()
root.geometry('500x500')
player1 = Label(root,text="Player 1").place(x='10',y='10')
player2 = Label(root,text="Player 2").place(x='250',y='10')
rock1 = Button(root, text = 'Rock', command = '').place(x='10',y='30')
rock2 = Button(root, text = 'Rock', command = '').place(x='250',y='30')
paper1 = Button(root, text = 'Paper', command = '').place(x='50',y='30')
paper2 = Button(root, text = 'Paper', command = '').place(x='300',y='30')
scissor1 = Button(root, text = 'Scissor', command = '').place(x='100',y='30')
scissor2 = Button(root, text = 'Scissor', command = '').place(x='350',y='30')
scores = Label(root,text="Scores").place(x='10',y='50')
root.mainloop()
