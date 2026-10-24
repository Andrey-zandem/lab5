import tkinter as tk


def exit_app() -> None:
    """Функция для закрытия приложения."""
    root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Пример с меню")
    root.geometry("300x200")

    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=exit_app)
    menu_bar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menu_bar)

    root.mainloop()
