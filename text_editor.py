#this program is written by muhammad yousaf Email:yousafsahiwal3@gmail.com
import subprocess
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:

    def __init__(self, root):
        
        self.root = root
        self.root.title("Python Text Editor By Muhammad yousaf")
        self.root.geometry("800x600")

        self.filename = None

        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand=1, fill="both")

        self.create_menu()
        self.create_terminal()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)
        menubar.add_cascade(label="File", menu=file_menu)

        run_menu = tk.Menu(menubar, tearoff=0)
        run_menu.add_command(label="Run", command=self.run_code)
        menubar.add_cascade(label="Run", menu=run_menu)

    def create_terminal(self):
        self.terminal_frame = tk.Frame(self.root)
        self.terminal_frame.pack(fill="x", side="bottom")

        self.terminal_text = tk.Text(self.terminal_frame, height=10, wrap="word", bg="black", fg="white")
        self.terminal_text.pack(expand=1, fill="both")

    def new_file(self):
        self.filename = None
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def exit_editor(self):
        self.root.quit()

    def run_code(self):
        if not self.filename:
            messagebox.showerror("Save your file", "Please save your code before running.")
            return

        self.save_file()

        self.terminal_text.delete(1.0, tk.END)
        try:
            result = subprocess.run(["python", self.filename], capture_output=True, text=True, shell=True)
            self.terminal_text.insert(1.0, result.stdout + result.stderr)
        except Exception as e:
            self.terminal_text.insert(1.0, str(e))

if __name__ == "__main__":
    screen = tk.Tk()
    editor = TextEditor(screen)
    screen.mainloop()
