from tkinter import *
import random

layout = Tk()
layout.title('gerador de senhas')

def gera_senha():
    p = ("abcdefghijklmnopqrstuvwxyz0123456789@#$%&ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    senha = random.sample(p, 8)

    resultado = f'''
    sua senha eh:\n{senha}'''

    resultado = resultado.replace("'",'')
    resultado = resultado.replace(",",'')
    resultado = resultado.replace('[', ' ')
    resultado = resultado.replace(']', ' ')

    texto['text'] = resultado


botao = Button(layout, text='gerar senha',
command=gera_senha, height=2, width=30, bg='MediumSeaGreen', fg='white', font='Verdana').place(x= 90, y=300)
texto = Label(layout, text='', fg='white', font='verdana', )
texto.place(x=90, y=370)
texto.config(background='gray', height=4, width=30)
    
layout.geometry('460x700')
layout.resizable(width=0, height=0)
layout.config(background='Aquamarine')


layout.mainloop()