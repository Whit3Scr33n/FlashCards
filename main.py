import tkinter as tk
from tkinter import ttk
from random import randint
import process
import output


def main():
    window = tk.Tk()
    window.title("Flash Cards")
    window.geometry("300x380")

    app = FlashCards(window)

    window.mainloop()


class FlashCards:
    def __init__ (self, window):
        self.names: list = []
        self.links_headers: dict = {}
        self.names, self.links_headers = output.links_headers()
        
        self.words: list = []
        self.count: int = 0
        self.side: int = 0
        
        self.window = window
        self.create_widgets()
    
    
    def select_cards_set(self, event):
        self.count = 0
        self.header = self.cards_set.get()
        self.link = self.links_headers[self.header]
        self.words = output.get_word_pairs(self.link)
        self.word.config(text = self.words[0][0])
        
    
    def prev_word(self):
        if self.count > 0:
            self.count -= 1
            self.side = 0
            self.word.config(text = self.words[self.count][self.side])
    
    
    def next_word(self):
        if self.count <= len(self.words)-2 and len(self.words) != 0:
            self.count += 1
            self.side = 0
            self.word.config(text = self.words[self.count][self.side])
    
    
    def turn(self):
        if len(self.words) > 0:
            if self.side == 1:
                self.side = 0
            else:
                self.side = 1
            self.word.config(text = self.words[self.count][self.side])
            
            
    def get_random(self):
        self.rand: int = self.count
        if len(self.words) > 0:
            while self.rand == self.count:
                self.rand = randint(0, len(self.words) - 1)
            self.count = self.rand
            self.side = 0
            self.word.config(text = self.words[self.count][self.side])
    
    
    def create_widgets(self):

# List of topics
        self.cards_set = ttk.Combobox(self.window, values=self.names, state='readonly', font=("Comic Sans MS", 12), width=38, height=20)
        self.cards_set.pack()
        self.cards_set.current(0)
        self.cards_set.bind('<<ComboboxSelected>>', self.select_cards_set)
    
    
# Show the word
        self.word = tk.Label(self.window, text="Select a words set", font=("Comic Sans MS", 18), width=60, height=4)
        self.word.pack()
    
    
# Previous item
        self.the_prev = tk.Button(self.window, text="Prev <<", command=self.prev_word, font=("Comic Sans MS", 11), fg = 'green', activeforeground = 'gray')
        self.the_prev.pack(side = 'bottom', pady = 6)
    
    
# Turn card
        self.turn = tk.Button(self.window, text="Turn", command=self.turn, font=("Comic Sans MS", 11), fg = 'orange', activeforeground = 'gray')
        self.turn.pack(side = 'bottom', pady = 6)
    
    
# Next item
        self.the_next = tk.Button(self.window, text="Next >>", command=self.next_word, font=("Comic Sans MS", 11), fg = 'green', activeforeground = 'gray')
        self.the_next.pack(side = 'bottom', pady = 6)
        
# Random item
        self.a_random = tk.Button(self.window, text="Random", command=self.get_random, font=("Comic Sans MS", 11), fg = 'dark blue', activeforeground = 'gray')
        self.a_random.pack(side = 'bottom', pady = 6)


if __name__ == '__main__':
    main()
    
    