import hashlib
import os.path
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import tkinter as tk
import csv


def get_path():
    path = fd.askopenfilename()
    return path


def insert_path():
    entry_path.delete('0', 'end')
    entry_path.insert('0', get_path())


def show_error():
    msg = f'Необходимо выбрать файл в формате "csv".'
    mb.showerror('Ошибка', msg)


def show_message(text_title, text_message):
    mb.showinfo(text_title, text_message)


def get_phone_numbers(file_name):
    phone_numbers = []
    if file_name == '':
        show_message('Ошибка', 'Не указан файл для обработки!')
    else:
        if os.path.splitext(file_name)[-1][1::] in ['csv']:
            with open(file_name, 'r', encoding='utf-8') as f:
                fields = ['sn', 'phone_number']
                reader = csv.DictReader(f, fields, delimiter=';')
                for row in reader:
                    phone_numbers.append(row['phone_number'])
            return phone_numbers
        else:
            show_error()


def convert_phone_number(phone_number):
    return hashlib.md5(phone_number.encode()).hexdigest()


def write_to_file(file_name, encrypted_numbers):
    new_file_name = f'{os.path.splitext(file_name)[0]}_encrypted{os.path.splitext(file_name)[1]}'
    with open(new_file_name, 'w', encoding='utf-8', newline='') as f:
        fields = ['sn', 'hash']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for encrypted_number in encrypted_numbers:
            writer.writerow(encrypted_number)


def get_converted_phone_numbers(phone_numbers):
    converted_phone_numbers = []
    for index, phone_number in enumerate(phone_numbers):
        converted_phone_numbers.append({'sn': index, 'hash': convert_phone_number(phone_number)})
    return converted_phone_numbers


def prepare_phone_numbers():
    phone_numbers = get_phone_numbers(entry_path.get())
    converted_phone_numbers = get_converted_phone_numbers(phone_numbers)
    write_to_file(entry_path.get(), converted_phone_numbers)
    show_message('', 'Файл успешно поготовлен!')


root = tk.Tk()
root.title('Подготовка файла')
root.geometry('300x150')
lbl_name = tk.Label(root,
                    text='Выберите файл со списком номеров телефонов\nдля отправки на проверку:',
                    width=50, height=2, anchor='w')
entry_path = tk.Entry(root, width=35)
button_browse = tk.Button(root, text='Обзор', width=7, command=insert_path)
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
