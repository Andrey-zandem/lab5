import time
import tkinter as tk


start_time: float | None = None
is_running: bool = False
elapsed: float = 0.0


def format_time(total_seconds: float) -> str:
    """Преобразует секунды в строку HH:MM:SS."""
    total = int(total_seconds)
    hours = total // 3600
    minutes = (total % 3600) // 60
    seconds = total % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def tick() -> None:
    """Обновляет метку и планирует следующий тик."""
    global elapsed

    if not is_running:
        return

    elapsed = time.time() - start_time
    label.config(text=format_time(elapsed))
    root.after(100, tick)


def start() -> None:
    """Запускает или продолжает счёт."""
    global start_time, is_running

    if is_running:
        return

    start_time = time.time() - elapsed
    is_running = True
    tick()


def stop() -> None:
    """Ставит на паузу. elapsed сохраняется для продолжения."""
    global is_running
    is_running = False


def reset() -> None:
    """Обнуляет всё."""
    global start_time, is_running, elapsed

    is_running = False
    start_time = None
    elapsed = 0.0
    label.config(text="00:00:00")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Секундомер")
    root.geometry("320x160")

    label = tk.Label(root, text="00:00:00", font=("Arial", 24))
    label.grid(row=0, column=0, columnspan=3, sticky="ew", pady=15)

    start_btn = tk.Button(root, text="Старт", command=start)
    stop_btn = tk.Button(root, text="Стоп", command=stop)
    reset_btn = tk.Button(root, text="Сброс", command=reset)

    start_btn.grid(row=1, column=0, sticky="ew", padx=3, pady=5)
    stop_btn.grid(row=1, column=1, sticky="ew", padx=3, pady=5)
    reset_btn.grid(row=1, column=2, sticky="ew", padx=3, pady=5)

    for i in range(3):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()