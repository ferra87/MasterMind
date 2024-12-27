import random
from tkinter import *


def genera_numero():
    lista = []

    numero1 = random.randint(0, 9)
    lista.append(numero1)

    numero2 = random.randint(0, 9)
    while numero2 == numero1:
        numero2 = random.randint(0, 9)
    lista.append(numero2)

    numero3 = random.randint(0, 9)
    while numero3 == numero2 or numero3 == numero1:
        numero3 = random.randint(0, 9)
    lista.append(numero3)

    numero4 = random.randint(0, 9)
    while numero4 == numero3 or numero4 == numero2 or numero4 == numero1:
        numero4 = random.randint(0, 9)
    lista.append(numero4)

    return lista


def button_pressed(num):
    global riga, colonna, valore, risultato
    if not vittoria() and riga < 9 and colonna <= 3:
        valore.append(num)
        griglia[riga][colonna].config(text=num)
        if colonna == 3:
            colonna = 0
            valore = riduci(valore)
            controllo(valore)
            valore.clear()
            riga += 1
        else:
            colonna += 1
    if vittoria():
        risultato.config(bg='green', text=numero)
    else:
        lista_controllo.clear()
    if riga == 9 and not vittoria():
        risultato.config(bg='red', text=numero)


def riduci(valore):
    for n in range(len(valore)):
        if valore[n] != '' and valore[n] == numero[n]:
            for j in range(len(valore)):
                if valore[n] == valore[j] and n != j:
                    valore[j] = ''
    for n in range(len(valore)):
        if valore[n] != '':
            for j in range(len(valore)):
                if valore[n] == valore[j] and n != j:
                    valore[j] = ''
    return valore


def controllo(valore):
    print(valore)
    print(numero)
    for i in range(len(valore)):
        if valore[i] == numero[i]:
            lista_controllo.append(1)
        elif valore[i] in numero:
            lista_controllo.append(0)
    lista_controllo.sort()
    lista_controllo.reverse()
    print(lista_controllo)
    for n in range(len(lista_controllo)):
        if lista_controllo[n] == 1:
            check[riga][n].config(bg='green')
        if lista_controllo[n] == 0:
            check[riga][n].config(bg='yellow')


def vittoria():
    if len(lista_controllo) == 4:
        if lista_controllo[0] == lista_controllo[1] == lista_controllo[2] == lista_controllo[3] == 1:
            return True
        else:
            return False
    else:
        return False


def reset():
    global numero, lista_controllo, riga, colonna, valore
    numero = genera_numero()
    riga = 0
    colonna = 0
    valore = []
    lista_controllo = []
    risultato.config(text='', bg='#aaa')
    for row in range(9):
        for column in range(4):
            griglia[row][column].config(text='')
            check[row][column].config(bg='#aaa')


window = Tk()
window.title('MasterMind')
window.geometry('600x600')
window.config(bg='#9d9d9d')

numero = genera_numero()
riga = 0
colonna = 0

griglia = [['' for i in range(4)] for i in range(9)]
valore = []
lista_controllo = []
bottoni = ['' for i in range(10)]
check = [['' for i in range(4)] for i in range(9)]

frame_griglia = Frame(window, bg='#9d9d9d')
frame_griglia.pack()
for row in range(9):
    for column in range(4):
        griglia[row][column] = Label(frame_griglia, text='', font=('Ink Free', 30), width=2, height=1, bg='#aaa', bd=5, relief='sunken')
        griglia[row][column].grid(row=row, column=column)
        check[row][column] = Label(frame_griglia, width=3, height=1, bg='#aaa', bd=5, relief='ridge')
        check[row][column].grid(row=row, column=column + 4)

risultato = Label(frame_griglia, font=('Ink Free', 30), bg='#aaa', width=10, height=1)
risultato.grid(row=10, column=0, columnspan=4)

rigioca = Button(frame_griglia, font=('Ink Free', 30), text='rigioca', bg='#aaa', width=9, height=1,
                 command=lambda: reset())
rigioca.grid(row=10, column=4, columnspan=4)

frame_bottoni = Frame(window)
frame_bottoni.pack()

bottoni[0] = Button(frame_bottoni, text='0',  width=7, height=2, font=35,
                    command=lambda: button_pressed(0))
bottoni[0].grid(row=0, column=0)
bottoni[1] = Button(frame_bottoni, text='1',  width=7, height=2, font=35,
                    command=lambda: button_pressed(1))
bottoni[1].grid(row=0, column=1)
bottoni[2] = Button(frame_bottoni, text='2',  width=7, height=2, font=35,
                    command=lambda: button_pressed(2))
bottoni[2].grid(row=0, column=2)
bottoni[3] = Button(frame_bottoni, text='3',  width=7, height=2, font=35,
                    command=lambda: button_pressed(3))
bottoni[3].grid(row=0, column=3)
bottoni[4] = Button(frame_bottoni, text='4',  width=7, height=2, font=35,
                    command=lambda: button_pressed(4))
bottoni[4].grid(row=0, column=4)
bottoni[5] = Button(frame_bottoni, text='5',  width=7, height=2, font=35,
                    command=lambda: button_pressed(5))
bottoni[5].grid(row=1, column=0)
bottoni[6] = Button(frame_bottoni, text='6',  width=7, height=2, font=35,
                    command=lambda: button_pressed(6))
bottoni[6].grid(row=1, column=1)
bottoni[7] = Button(frame_bottoni, text='7',  width=7, height=2, font=35,
                    command=lambda: button_pressed(7))
bottoni[7].grid(row=1, column=2)
bottoni[8] = Button(frame_bottoni, text='8',  width=7, height=2, font=35,
                    command=lambda: button_pressed(8))
bottoni[8].grid(row=1, column=3)
bottoni[9] = Button(frame_bottoni, text='9',  width=7, height=2, font=35,
                    command=lambda: button_pressed(9))
bottoni[9].grid(row=1, column=4)

window.mainloop()
