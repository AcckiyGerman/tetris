import tkinter as tk
from tkinter import ttk
import random

class TetrisGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tetris")
        
        # Colors for tetrominos
        self.colors = ['cyan', 'yellow', 'purple', 'blue', 'orange', 'green', 'red']
        
        # Game constants
        self.BOARD_WIDTH = 10
        self.BOARD_HEIGHT = 20
        self.BLOCK_SIZE = 30
        
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create canvas
        canvas_width = self.BOARD_WIDTH * self.BLOCK_SIZE
        canvas_height = self.BOARD_HEIGHT * self.BLOCK_SIZE
        self.canvas = tk.Canvas(
            main_frame,
            width=canvas_width,
            height=canvas_height,
            bg='black'
        )
        self.canvas.grid(row=0, column=0, padx=5, pady=5)
        
        # Create game board matrix (0 means empty)
        self.board = [[0 for _ in range(self.BOARD_WIDTH)] 
                     for _ in range(self.BOARD_HEIGHT)]
        
        # Draw grid lines
        self.draw_grid()
        
        # Bind keyboard events
        self.root.bind('<Left>', lambda e: self.move_left())
        self.root.bind('<Right>', lambda e: self.move_right())
        self.root.bind('<Down>', lambda e: self.move_down())
        self.root.bind('<Up>', lambda e: self.rotate())
        
        # Center the window
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')

    def draw_grid(self):
        # Draw vertical lines
        for i in range(self.BOARD_WIDTH + 1):
            x = i * self.BLOCK_SIZE
            self.canvas.create_line(
                x, 0, x, self.BOARD_HEIGHT * self.BLOCK_SIZE,
                fill='gray'
            )
        
        # Draw horizontal lines
        for i in range(self.BOARD_HEIGHT + 1):
            y = i * self.BLOCK_SIZE
            self.canvas.create_line(
                0, y, self.BOARD_WIDTH * self.BLOCK_SIZE, y,
                fill='gray'
            )

    def move_left(self):
        print("Move left")
        # TODO: Implement piece movement

    def move_right(self):
        print("Move right")
        # TODO: Implement piece movement

    def move_down(self):
        print("Move down")
        # TODO: Implement piece movement

    def rotate(self):
        print("Rotate")
        # TODO: Implement piece rotation

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TetrisGame()
    game.run()
