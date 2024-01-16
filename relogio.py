import tkinter as tk
from tkinter import *
import os
from time import strftime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

root = tk.Tk()
root.title('Seu relógio')
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background='#8A2BE2')


def toggle_dark_mode():
    if root['bg'] == '#8A2BE2':
        root['bg'] = 'white'
        tela['bg'] = 'white'
        saudacao['bg'] = 'white'
        data['bg'] = 'white'
        horas['bg'] = 'white'
    else:
        root['bg'] = '#8A2BE2'
        tela['bg'] = '#8A2BE2'
        saudacao['bg'] = '#8A2BE2'
        data['bg'] = '#8A2BE2'
        horas['bg'] = '#8A2BE2'


def get_saudacao():
    current_hour = int(strftime('%H'))
    if current_hour < 12:
        saudacao_text = 'Bom dia, manu!'
    elif current_hour < 18:
        saudacao_text = 'Boa tarde, manu!'
    else:
        saudacao_text = 'Boa noite, manu!'
    saudacao.config(text=saudacao_text, fg='black', font=('Macaroni', 24, 'italic'))


def get_data():
    data_atual = strftime(' %d de %B de %Y')
    data.config(text=data_atual, fg='black', font=('Macaroni', 14, 'italic'))


def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual, fg='black', font=('Montserrat', 64, 'bold italic'))
    horas.after(1000, get_horas)


tela = tk.Canvas(root, width=600, height=20, bg='#8A2BE2', bd=0, highlightthickness=0, relief='ridge')
tela.pack()
saudacao = Label(root, bg='#8A2BE2', fg='black', font=('Macaroni', 24, 'italic'))
saudacao.pack()
data = Label(root, bg='#8A2BE2', fg='black', font=('Macaroni', 14, 'italic'))
data.pack(pady=2)
horas = Label(root, bg='#8A2BE2', fg='black', font=('Montserrat', 64, 'bold italic'))
horas.pack(pady=2)
get_saudacao()
get_data()
get_horas()
root.mainloop()
