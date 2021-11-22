from tkinter import *
from tkinter import ttk
from tkinter import Image
from tkinter import filedialog

root = Tk()
root.geometry('950x500+300+150')
root.resizable(width=True, height=True)

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text='Welcome in Poker game', foreground='blue', background='white').grid(column=0, row=0)

ttk.Button(frm, text="Go", command=root.destroy).grid(column=3, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=2)


root.mainloop()

numbers = {
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A',
}
suits = {
    'H': u'\u2665',  # Hearts
    'D': u'\u2666',  # Diamonds
    'C': u'\u2663',  # Clubs
    'S': u'\u2660',  # Spades
}

#Cards Generator

def build_deck():
    numbers = list(range(2,15))
    suits = ['H', 'D', 'C', 'S']
    deck = []
    for i in numbers:
        for s in suits:
            card = s+str(i)
            deck.append(card)
    return deck
print(build_deck())



