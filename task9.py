import tkinter as tk 
import random


COLORS = ["red", "green", "blue", "yellow", "orange", "purple", "cyan", "magenta"]


def change_color() -> None:
    """Меняет цвет панели на случайный из списка."""
    new_color = random.choice(COLORS)
    panel.config(bg=new_color)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Цветовая панель")
    root.geometry("400x400")

    panel = tk.Frame(root, bg="gray", width=300, height=200)
    panel.pack(pady=20, padx=20, fill="both", expand=True)

    button = tk.Button(root, text="Сменить цвет", command=change_color)
    button.pack(pady=10)

    root.mainloop()

