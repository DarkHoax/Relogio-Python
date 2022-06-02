from cProfile import label
from time import time
from tkinter import *
import tkinter
from datetime import datetime
import pyglet

pyglet.font.add_file("digital-7.ttf")

preto = "#3d3d3d" #Cor1
branco = "#fafcff" #Cor2
verde = "#42c920" #Cor3
vermelha = "#eb463b" #Cor4
cinza = "#dedcdc" #Cor5
azul = "#3080f0" #Cor6

fundo = preto
cor = verde

janela = Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=preto)

def Relogio():
    #DATAS
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")
    
    l1.config(text=hora)
    l1.after(200, Relogio)
    l2.config(text=semana +" "+ str(dia) + "/"+ str(mes) + "/" + str(ano))

#HORA
l1 = Label(janela, text="", font=("digital-7 70"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

#MES
l2 = Label(janela, text="10:50:22", font=("digital-7 20"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)



Relogio()
janela.mainloop()