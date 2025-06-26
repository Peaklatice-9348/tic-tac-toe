from tkinter import *
from functools import partial
import copy

window = Tk()
window.title('tic tac toe')
buttons = []
turn='x'

def restart():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=DISABLED)

def check_winner():
    for i in range(3):

        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return buttons[i][0]['text']
        
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return buttons[0][i]['text']
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return buttons[0][0]['text']
    
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return buttons[1][1]['text']

    return None

def box(row,column):
    global turn
    if buttons[row][column]['text'] == '':
        buttons[row][column].config(text=turn)
        winner = check_winner()
        if winner:
            label.config(text=f'player {winner} wins!')
            restart()
        elif all(all(cell['text'] != '' for cell in row)for row in buttons):
            label.config(text='Draw!')
            restart()
        else:
            if turn == 'x':
                turn = 'o'
            else:
                turn='x'
            label.configure(text=f"Player {turn}'s turn")

for i in range(3):
    row=[]
    for j in range(3):
        button = Button(window,width=20,height=8,command=partial(box,i,j),font=20)
        button.grid(row=i,column=j)
        row.append(button)
    buttons.append(row)
label = Label(window, text="Player X's turn", font=('Arial', 18))
label.grid(row=3,column=0,columnspan=3)

window.mainloop()