import tkinter as tk 

BUTTONS = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
]


def on_click(symbol: str) -> None:
    """Обработчик нажатия любой кнопки калькулятора."""
    current = entry.get()
    if symbol == "C":
        entry.delete(0, tk.END)
    elif symbol == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Ошибка")
    else:
        entry.insert(tk.END, symbol)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Калькулятор")

    entry = tk.Entry(root, font=("Arial", 16), justify="right")
    entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

    for row_index, row in enumerate(BUTTONS):
        for col_index, symbol in enumerate(row):
            btn = tk.Button(
                root,
                text=symbol,
                font=("Arial", 14),
                command=lambda symbol=symbol: on_click(symbol),
            )
            btn.grid(
                row=row_index + 1,
                column=col_index,
                sticky="nsew",
                padx=2,
                pady=2,
            )

    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    for i in range(1, 5):
        root.grid_rowconfigure(i, weight=1)

    root.mainloop()