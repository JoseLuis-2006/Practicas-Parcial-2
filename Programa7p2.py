from tkinter import *
from tkinter import messagebox
import random
# importae libreria random

class Principal():
    def __init__(self): 
         # Crear ventana principal / Create main window
        self.ven = Tk() 
        self.ven.title('Programa 10 con Ventanas')  # Título de la ventana / window title
        self.ven.geometry('550x250')  # Tamaño de la ventana / window size
        # todo debe ir dentro de aquí / everything must go inside this window
        # pack solo permite un elemento por renglón / pack only allows one element per(x
        # Label(ven, text = "Hola mundo").pack()
        self.lista = []
        # self.inicio()  # Llama al método que crea los widgets / calls the method that creates the widgets
        self.a = 0
        self.b = 0
        self.lista = []
        self.aux1 = 0
        self.aux2 = 0
        self.con = 0

    def inicio(self):

        # Label(self.ven,text="Programa 9").place(x = 1, y =2)
        l1 = Label(self.ven,text="Programa 10")
        l1.place(x = 200, y = 20)
        l2 = Label(self.ven,text="Escribe un numero")
        l2.place(x = 100, y = 50)
        self.n1 = Entry(self.ven)
        self.n1.place(x = 100, y = 75)
        l3 = Label(self.ven,text="Escribe otro numero")
        l3.place(x = 250, y =50)
        self.n2 = Entry(self.ven)
        self.n2.place(x=250, y =75)
        b1 = Button(self.ven, text="Agregar", command=self.agregar)
        b1.place(x=100, y =120)
        b2 = Button(self.ven, text="Mayor",command=self.mayor)
        b2.place(x=180, y =120)
        b3 = Button(self.ven, text="Menor", command=self.menor)
        b3.place(x=260, y =120)
        b4 = Button(self.ven, text="Salir", command=self.salir)
        b4.place(x=340, y =120, width = 50)
        self.listaElem = Label(self.ven,text=" ")
        self.listaElem.place(x = 20, y =200)
        self.listview = Listbox(self.ven, width= 15, bg= "black", activestyle= "dotbox", fg="white")
        self.listview.place(x=420, y = 20)
        self.ven.mainloop()
    
    def salir(self):
        self.ven.destroy() # destruimos ventana 

    def mayor(self):
        if len(self.lista) > 0:
            if self.aux1 < self.lista[self.con]:
                self.aux1 = self.lista[self.con]
            self.con += 1
            if len(self.lista) -1 == self.con:
                messagebox.showinfo("El Mayor", f"El mayor es: {self.aux1}")
                self.con = 0
            else:
                return self.mayor()
            #self.con += 1
        else:
            messagebox.showerror("Error", "Lista vacia")

    # def menor(self,n):

    #     if self.aux > self.lista[n] 

    def menor(self):
        if len(self.lista) > 0:
            self.aux2 = self.lista[0]
            for i in self.lista:
                if self.aux2 > i:
                    self.aux2 = i
            messagebox.showinfo("El Menor",f"El menor es {self.aux2}")
        else:
            messagebox.showerror("Error", "Lista vacia")


    
    def agregar(self):
        try:
            # self.a = int(self.n1.get())
            self.a = random.randint(1,100)
            self.lista.append(self.a)
            self.listview.insert((self.listview.size() + 1),self.a)
            # self.n1.delete(0,END)
            # self.b = int(self.n2.get())
            # self.lista.append(self.b)
            # self.listview.insert((self.listview.size() + 1),self.b)
            # self.n2.delete(0,END)

            self.listaElem.config(text=f"La lista: {self.lista}")
            self.aux1 = self.lista[0]
            self.listview.insert(self.a)


            # print(self.lista)

        except ValueError:
             messagebox.showerror("Error", "Algun dato no es numero")


if __name__ == "__main__":
    app = Principal()
    app.inicio()