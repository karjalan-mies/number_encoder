import tkinter as tk
from utils import write_path, prepare_phone_numbers

root = tk.Tk()
root.title('Подготовка файла')
root.geometry('300x150')
lbl_name = tk.Label(root,
                    text='Выберите файл со списком номеров телефонов\nдля отправки на проверку:',
                    width=50, height=2, anchor='w')
entry_path = tk.Entry(root, width=35)
button_browse = tk.Button(root, text='Обзор', width=7, command=write_path)
button_encrypt = tk.Button(root, text='Зашифровать файл', width=18, command=prepare_phone_numbers)
button_send = tk.Button(root, text='Отправить файл', width=18)
button_close = tk.Button(root, text='Закрыть', width=7, command=root.destroy)

lbl_name.place(x=10, y=5)
entry_path.place(x=10, y=50)
button_browse.place(x=230, y=47)
button_encrypt.place(x=10, y=80)
button_send.place(x=152, y=80)
button_close.place(x=230, y=115)

root.mainloop()
