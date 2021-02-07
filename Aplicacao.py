# -*- coding: utf-8 -*-

#ComboBox https://www.delftstack.com/pt/tutorial/tkinter-tutorial/tkinter-combobox/

#Não tá apagando no DB

try:
    from Tkinter import *
except ImportError:         ## Python 3
    from tkinter import *
    
from tkinter import messagebox
import tkinter as tk
import sqlite3


root = Tk()
root.title("Printer 3D - Materiais")
root.resizable(0, 0)


class Main:
    
    def __init__(self,master):

        self.frame = Frame(master)
        self.frame.pack()
        Label(self.frame, text="Printer 3D - Materiais", font=(None, 15)).pack()

        self.separador = Frame(self.frame, height=2,bd=3,relief=SUNKEN,width=100)
        self.separador.pack(fill=X, pady=5, padx=2)
        
        self.frame2 = Frame(master)
        self.frame2.pack()  
        self.add = Button(self.frame2, text="Novo",command=bt_iniciar, width=15)
        self.add.pack(side=LEFT)
        self.apagar = Button(self.frame2, text="Excluir",command=self.apagar, width=15)
        self.apagar.pack(side=LEFT)
        Label(self.frame2, text=" ", width=40).pack()

        self.frame3 = Frame(master)
        self.frame3.pack(side="left")  
        self.lancamento = Entry(self.frame3,width=15)
        self.lancamento.pack(side="bottom")
        self.lancamento = Entry(self.frame3,width=15)
        self.lancamento.pack(side="bottom")
        self.lancamento = Entry(self.frame3,width=15)
        self.lancamento.pack(side="bottom")
        
        scrollbar = Scrollbar(master)
        scrollbar.pack(fill=Y, side=RIGHT)
        scrollbar.config(command = self.yview)
        
        self.listbox = Listbox(master, width=30, height=15, yscrollcommand = scrollbar.set)
        self.listbox.pack(padx=5,pady=5)
        self.listbox.place(x = 25, y = 80)
      
        self.listbox2 = Listbox(master, width=30, height=15, yscrollcommand = scrollbar.set)
        self.listbox2.pack(padx=5,pady=5)
        self.listbox2.place(x = 220, y = 80)


#---------------------------------------------------------------

        #Criar banco de dados
        self.conectar = sqlite3.connect("notas.db")
        self.cursor = self.conectar.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS notas(name TEXT)")
        self.conectar.commit()
        lista = self.cursor.execute("SELECT name FROM notas")
        for i in lista:
                self.listbox.insert(END, i)
                
        lista2 = self.cursor.execute("SELECT qtd FROM notas")
        for j in lista2:
                self.listbox2.insert(END, j)
                
#---------------------------------------------------------------
                
    def yview(self, *args):
        self.listbox.yview(*args)
        self.listbox2.yview(*args)
        
    def apagar(self):
        lancamentoy = str(self.listbox.get(ACTIVE))[3:-3]
        #sql = "DELETE FROM notas WHERE name = " + "'" + lancamentoy + "'"

        self.cursor.execute("DELETE notas FROM name,qtd WHERE name =\"%s\";" %(lancamentoy,))
        
    
        #self.cursor.execute(sql,(lancamentoy,))

        self.conectar.commit()
        self.listbox.delete(ANCHOR)  

        
def bt_iniciar():
    janela2 = Tk()
    janela2.title("Cadastro Material")
    
    Label(janela2, text="Nome - Data - Qtd").pack()
    janela2.lancamento = Entry(janela2,width=15)
    janela2.lancamento.pack(side="left")
    janela2.lancamento2 = Entry(janela2,width=15)
    janela2.lancamento2.pack(side="left")

    janela2.geometry("450x300+700+350")
    janela2.mainloop()

def adicionar():
    lancamentox = lancamento.get()
    if lancamentox == "":
        messagebox.showinfo("Error","Por Favor insira uma nota")
    else:
        master.cursor.execute("INSERT INTO notas (name) VALUES(?)",(lancamentox,))
        master.conectar.commit()
        master.listbox.insert(END, lancamentox)
        master.lancamento.delete(0,END)

  




root.geometry("500x350+500+300")
Main(root)
root.mainloop()

