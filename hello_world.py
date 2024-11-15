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
        
        # Define tetromino shapes
        self.SHAPES = {
            'I': [[1, 1, 1, 1]],
            'O': [[1, 1],
                  [1, 1]],
            'T': [[0, 1, 0],
                  [1, 1, 1]],
            'S': [[0, 1, 1],
                  [1, 1, 0]],
            'Z': [[1, 1, 0],
                  [0, 1, 1]],
            'J': [[1, 0, 0],
                  [1, 1, 1]],
            'L': [[0, 0, 1],
                  [1, 1, 1]]
        }
        
        # Current piece state
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.current_shape = None
        self.current_color = None
        
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
        
        # Create first piece
        self.create_new_piece()
        
        # Bind keyboard events
        self.root.bind('<Left>', lambda e: self.move_left())
        self.root.bind('<Right>', lambda e: self.move_right())
        self.root.bind('<Down>', lambda e: self.move_down())
        self.root.bind('<Up>', lambda e: self.rotate())
        
        # Start the game loop
        self.update_game()
        
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

    def create_new_piece(self):
        # Choose a random shape and color
        shape_name = random.choice(list(self.SHAPES.keys()))
        self.current_shape = self.SHAPES[shape_name]
        self.current_color = self.colors[list(self.SHAPES.keys()).index(shape_name)]
        
        # Starting position (centered at top)
        self.current_x = self.BOARD_WIDTH // 2 - len(self.current_shape[0]) // 2
        self.current_y = 0
        
        # Draw the piece
        self.draw_piece()

    def draw_piece(self):
        # Clear previous piece (if any)
        self.canvas.delete("piece")
        
        # Draw current piece
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    self.draw_block(
                        self.current_x + x,
                        self.current_y + y,
                        self.current_color,
                        "piece"
                    )

    def draw_block(self, x, y, color, tag):
        x1 = x * self.BLOCK_SIZE
        y1 = y * self.BLOCK_SIZE
        x2 = x1 + self.BLOCK_SIZE
        y2 = y1 + self.BLOCK_SIZE
        
        # Draw filled rectangle with black border
        self.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=color,
            outline="black",
            tags=tag
        )

    def check_collision(self, offset_x=0, offset_y=0, shape=None):
        if shape is None:
            shape = self.current_shape
            
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_x + x + offset_x
                    new_y = self.current_y + y + offset_y
                    
                    # Check board boundaries
                    if (new_x < 0 or new_x >= self.BOARD_WIDTH or
                        new_y >= self.BOARD_HEIGHT):
                        return True
                    
                    # Check collision with placed pieces
                    if new_y >= 0 and self.board[new_y][new_x]:
                        return True
        return False

    def move_left(self):
        if not self.check_collision(offset_x=-1):
            self.current_x -= 1
            self.draw_piece()

    def move_right(self):
        if not self.check_collision(offset_x=1):
            self.current_x += 1
            self.draw_piece()

    def move_down(self):
        if not self.check_collision(offset_y=1):
            self.current_y += 1
            self.draw_piece()
            return True
        else:
            self.place_piece()
            return False

    def place_piece(self):
        # Add the current piece to the board
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    board_y = self.current_y + y
                    board_x = self.current_x + x
                    if board_y >= 0:
                        self.board[board_y][board_x] = self.current_color
        
        # Redraw the entire board
        self.redraw_board()
        
        # Create a new piece
        self.create_new_piece()
        
        # Check if game is over
        if self.check_collision():
            print("Game Over!")
            self.root.quit()

    def redraw_board(self):
        # Clear the board on canvas
        self.canvas.delete("placed")
        
        # Draw all placed pieces
        for y, row in enumerate(self.board):
            for x, color in enumerate(row):
                if color:
                    self.draw_block(x, y, color, "placed")

    def update_game(self):
        # Move piece down automatically
        self.move_down()
        
        # Schedule next update (faster fall speed = lower number)
        self.root.after(1000, self.update_game)

    def rotate(self):
        # Get the rotated shape matrix
        rotated_shape = self.get_rotated_shape()
        
        # Check if rotation is possible
        if not self.check_collision(shape=rotated_shape):
            self.current_shape = rotated_shape
            self.draw_piece()

        # If rotation is not possible, try moving the piece to the left
        elif not self.check_collision(shape=rotated_shape, offset_x=-1):
            self.current_x -= 1
            self.current_shape = rotated_shape
            self.draw_piece()

    def get_rotated_shape(self):
        # Transpose the shape matrix
        rows = len(self.current_shape)
        cols = len(self.current_shape[0])
        rotated = [[0 for _ in range(rows)] for _ in range(cols)]
        
        # Rotate 90 degrees clockwise
        for row in range(rows):
            for col in range(cols):
                rotated[col][rows - 1 - row] = self.current_shape[row][col]
        
        return rotated

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TetrisGame()
    game.run()
