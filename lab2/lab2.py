import tkinter as tk
import webbrowser
import time

# Список и интервал
web_pages = []
interval = 0

# Показ сайтов
def show_web_pages():
    for url in web_pages:
        webbrowser.open(url)
        time.sleep(interval)

# Добавление новых сайтов в список
def add_web_page():
    new_url = url_entry.get()
    if new_url:
        web_pages.append(new_url)
        url_listbox.insert(tk.END, new_url)
        url_entry.delete(0, tk.END)

# Задаем интервал
def set_interval():
    global interval
    interval = int(interval_entry.get())
    interval_entry.delete(0, tk.END)

# Создаем окно
window = tk.Tk()
window.title("Показ сайтов")

# Создаем поле для ввода сайтов
add_frame = tk.Frame(window)
add_frame.pack(pady=10)

url_label = tk.Label(add_frame, text="Добавьте страницу:")
url_label.pack(side=tk.LEFT)

url_entry = tk.Entry(add_frame)
url_entry.pack(side=tk.LEFT)

add_button = tk.Button(add_frame, text="Добавить", command=add_web_page)
add_button.pack(side=tk.LEFT)

# Создаем поле для ввода интервала
interval_frame = tk.Frame(window)
interval_frame.pack()

interval_label = tk.Label(interval_frame, text="Интервал (сек):")
interval_label.pack(side=tk.LEFT)

interval_entry = tk.Entry(interval_frame)
interval_entry.pack(side=tk.LEFT)

set_interval_button = tk.Button(interval_frame, text="Задать интервал", command=set_interval)
set_interval_button.pack(side=tk.LEFT)

# Создаем поле для вывода списка
url_listbox = tk.Listbox(window)
url_listbox.pack()

# Создаем кнопку для запуска показа сайтов
start_button = tk.Button(window, text="Начать показ", command=show_web_pages)
start_button.pack(pady=10)

window.mainloop()