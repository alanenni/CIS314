import tkinter as tk
import random

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Game")
        self.cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
        random.shuffle(self.cards)
        self.buttons = []
        self.selected = []
        self.matches = 0

        for i in range(4):
            for j in range(4):
                button = tk.Button(master, text='', width=10, height=5,
                                   command=lambda row=i, col=j: self.choose_card(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

    def choose_card(self, row, col):
        index = 4 * row + col
        button = self.buttons[index]
        
        if button['text'] == '' and len(self.selected) < 2:
            button['text'] = self.cards[index]
            self.selected.append(index)
            
            if len(self.selected) == 2:
                self.master.after(500, self.check_match)

    def check_match(self):
        idx1, idx2 = self.selected
        if self.cards[idx1] == self.cards[idx2]:
            self.buttons[idx1]['state'] = 'disabled'
            self.buttons[idx2]['state'] = 'disabled'
            self.matches += 1
            if self.matches == 8:
                self.show_win_message()
        else:
            self.buttons[idx1]['text'] = ''
            self.buttons[idx2]['text'] = ''
        self.selected = []

    def show_win_message(self):
        win_window = tk.Toplevel(self.master)
        win_window.title("Congratulations!")
        tk.Label(win_window, text="You've won the game!", font=('Arial', 14)).pack(padx=20, pady=20)
        tk.Button(win_window, text="Play Again", command=self.reset_game).pack(pady=10)

    def reset_game(self):
        self.matches = 0
        random.shuffle(self.cards)
        for button in self.buttons:
            button['text'] = ''
            button['state'] = 'normal'

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()




























# colors = ("blue", "yellow", "red", "orange", "pink", "purple", "black", "brown", "white", "clear") #creates a tuple of colors 
# reversedColors = tuple(reversed(colors)) # creates a tuple of Colors reversed 
# print(colors)
# print(reversedColors)
# print("The third element of the tuple Colors is", colors[2])
# print("The third element of the tuple reversedColors is", reversedColors[2])
# colors = set(colors) # converts the tuple colors into a set in order to rendomize the items within 
# colors = tuple(colors) # converts the set colors back into a tuple 
# print("The tuple colors randomized: ", colors)

# colors = colors + ("gold", )
# print(colors)






















#file handling 
"""open()- allows for 2 arguments: <filename> + <model>
read() - full file 

mode can be:
    read: r (default)
    write: w 
    append: a
    create: x

mode can also be:
    text: t (default)
    binary: b 
"""