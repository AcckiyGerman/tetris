import tkinter as tk
from tkinter import ttk

class HelloWorldApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hello World")
        
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Add label
        ttk.Label(main_frame, text="Hello World!").grid(row=0, column=0, pady=10)
        
        # Add OK button
        ttk.Button(main_frame, text="OK", command=self.root.destroy).grid(row=1, column=0)
        
        # Center the window
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = HelloWorldApp()
    app.run()
