from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Таблица Шульте')
game_run = False
total = 0
field = []

def clear():
    for row in range(5):
        for col in range(5):
            field[row][col]['text'] = ''
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = False
    global total
    total = 0

def new_game():
    clear()
    for row in range(5):
        for col in range(5):
            field[row][col]['text'] = next_rnd()
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True

def next_rnd():
    while True:
        next = random.randint(1, 25)
        if not exists(next):
            return next

def exists(num):
    for row in range(5):
        for col in range(5):
            if field[row][col]['text'] == num :
                return True
    return False

def click(row, col):
    global total
    global game_run
    if game_run:
        if field[row][col]['text'] == total + 1 :
            field[row][col]['background'] = 'pink'
            total = total + 1
            if total >= 25 :
                messagebox.showinfo('Игра закончена', 'ПОЗДРАВЛЯЮ!') 
                clear()

for row in range(5):
    line = []
    for col in range(5):
        button = Button(root, text=' ' , width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)

new_button = Button(root, text='Новая игра', command=new_game)
new_button.grid(row=5, column=0, columnspan=3, sticky='nsew')

root.mainloop()