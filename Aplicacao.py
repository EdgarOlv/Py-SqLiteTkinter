# -*- coding: utf-8 -*-

from tkinter import *
import sqlite3
from tkinter import messagebox


class Main:
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack()
        Label(self.frame, text="Digite sua nota").pack()
        self.nota = Entry(self.frame,width=35)
        self.nota.pack()
        self.separador = Frame(height=2,bd=3,relief=SUNKEN,width=100)
        self.separador.pack(fill=X, pady=5, padx=5)
        self.frame3 = Frame(master)
        self.frame3.pack()  
        self.add = Button(self.frame3, text="Adicionar Nota",command=self.adicionar)
        self.add.pack(side=LEFT)
        self.apagar = Button(self.frame3, text="Apagar Nota",command=self.apagar)
        self.apagar.pack(side=LEFT)
        scrollbar = Scrollbar(master)
        scrollbar.pack(fill=Y, side=RIGHT)
        self.listbox = Listbox(master, width=50, height=20)
        self.listbox.pack(padx=5,pady=5)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        #Criar banco de dados
        self.conectar = sqlite3.connect("notas.db")
        self.cursor = self.conectar.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS notas(name TEXT)")
        self.conectar.commit()
        lista = self.cursor.execute("SELECT * FROM notas")
        for i in lista:
                self.listbox.insert(END, i)

    def adicionar(self):
        notax = self.nota.get()
        if notax == "":
            messagebox.showinfo("Error","Por Favor insira uma nota")
        else:
            self.cursor.execute("INSERT INTO notas VALUES(?)",(notax,))
            self.conectar.commit()
            self.listbox.insert(END, notax)
            self.nota.delete(0,END)

    def apagar(self):
        notay = str(self.listbox.get(ACTIVE))[3:-3]
        self.cursor.execute("DELETE FROM notas WHERE name=?",(notay,))
        self.conectar.commit()
        self.listbox.delete(ANCHOR)

root = Tk()
root.geometry("300x400")
Main(root)
root.mainloop()


