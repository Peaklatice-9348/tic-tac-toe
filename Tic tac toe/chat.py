from tkinter import *
from functools import partial

window = Tk()
window.title('Tic Tac Toe')
buttons = []

turn = 'X'

def box(row, column):
    global turn
    if buttons[row][column]['text'] == '':
        buttons[row][column].config(text=turn)

        turn = 'O' if turn == 'X' else 'X'


for i in range(3):
    row = []
    for j in range(3):
        button = Button(window, width=20, height=8, command=partial(box, i, j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

label = Label(window, text="Player X's turn", font=('Arial', 18))
label.grid(row=3, column=0, columnspan=3)

window.mainloop()
