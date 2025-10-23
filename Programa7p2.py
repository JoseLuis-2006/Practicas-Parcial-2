from tkinter import *  # Español: Importa todos los módulos de tkinter / English: Imports all tkinter modules
from tkinter import messagebox  # Español: Importa el módulo de cuadros de mensaje / English: Imports message boxes module
import random  # Español: Importa librería random / English: Imports random library
# Español: importar libreria random / English: import random library

class Principal():  # Español: Define la clase Principal / English: Defines the Main class
    def __init__(self):  # Español: Método constructor / English: Constructor method
         # Español: Crear ventana principal / English: Create main window
        self.ven = Tk()  # Español: Crea la ventana principal / English: Creates main window
        self.ven.title('Programa 10 con Ventanas')  # Español: Título de la ventana / English: Window title
        self.ven.geometry('550x250')  # Español: Tamaño de la ventana / English: Window size
        # Español: todo debe ir dentro de aquí / English: everything must go inside this window
        # Español: pack solo permite un elemento por renglón / English: pack only allows one element per row
        # Español: Label(ven, text = "Hola mundo").pack() / English: Label(ven, text = "Hello world").pack()
        self.lista = []  # Español: Crea lista vacía / English: Creates empty list
        # Español: self.inicio() - Llama al método que crea los widgets / English: self.inicio() - calls the method that creates the widgets
        self.a = 0  # Español: Variable para primer número / English: Variable for first number
        self.b = 0  # Español: Variable para segundo número / English: Variable for second number
        self.lista = []  # Español: Lista para almacenar números / English: List to store numbers
        self.aux1 = 0  # Español: Variable auxiliar para mayor / English: Auxiliary variable for maximum
        self.aux2 = 0  # Español: Variable auxiliar para menor / English: Auxiliary variable for minimum
        self.con = 0  # Español: Contador para recursividad / English: Counter for recursion

    def inicio(self):  # Español: Método para interfaz gráfica / English: Method for GUI interface

        # Español: Label(self.ven,text="Programa 9").place(x = 1, y =2) / English: Label(self.ven,text="Program 9").place(x = 1, y =2)
        l1 = Label(self.ven,text="Programa 10")  # Español: Crea título principal / English: Creates main title
        l1.place(x = 200, y = 20)  # Español: Posiciona título / English: Positions title
        l2 = Label(self.ven,text="Escribe un numero")  # Español: Label para primer número / English: Label for first number
        l2.place(x = 100, y = 50)  # Español: Posiciona label / English: Positions label
        self.n1 = Entry(self.ven)  # Español: Campo entrada primer número / English: First number entry field
        self.n1.place(x = 100, y = 75)  # Español: Posiciona campo / English: Positions field
        l3 = Label(self.ven,text="Escribe otro numero")  # Español: Label para segundo número / English: Label for second number
        l3.place(x = 250, y =50)  # Español: Posiciona label / English: Positions label
        self.n2 = Entry(self.ven)  # Español: Campo entrada segundo número / English: Second number entry field
        self.n2.place(x=250, y =75)  # Español: Posiciona campo / English: Positions field
        b1 = Button(self.ven, text="Agregar", command=self.agregar)  # Español: Botón agregar números / English: Add numbers button
        b1.place(x=100, y =120)  # Español: Posiciona botón agregar / English: Positions add button
        b2 = Button(self.ven, text="Mayor",command=self.mayor)  # Español: Botón encontrar mayor / English: Find maximum button
        b2.place(x=180, y =120)  # Español: Posiciona botón mayor / English: Positions maximum button
        b3 = Button(self.ven, text="Menor", command=self.menor)  # Español: Botón encontrar menor / English: Find minimum button
        b3.place(x=260, y =120)  # Español: Posiciona botón menor / English: Positions minimum button
        b4 = Button(self.ven, text="Salir", command=self.salir)  # Español: Botón salir / English: Exit button
        b4.place(x=340, y =120, width = 50)  # Español: Posiciona botón salir / English: Positions exit button
        self.listaElem = Label(self.ven,text=" ")  # Español: Label para mostrar lista / English: Label to show list
        self.listaElem.place(x = 20, y =200)  # Español: Posiciona label lista / English: Positions list label
        self.listview = Listbox(self.ven, width= 15, bg= "black", activestyle= "dotbox", fg="white")  # Español: Crea Listbox para números / English: Creates Listbox for numbers
        self.listview.place(x=420, y = 20)  # Español: Posiciona Listbox / English: Positions Listbox
        self.ven.mainloop()  # Español: Inicia bucle principal / English: Starts main loop
    
    def salir(self):  # Español: Método para cerrar ventana / English: Method to close window
        self.ven.destroy()  # Español: destruimos ventana / English: destroys window 

    def mayor(self):  # Español: Método para encontrar número mayor / English: Method to find maximum number
        if len(self.lista) > 0:  # Español: Verifica si lista no está vacía / English: Checks if list is not empty
            if self.aux1 < self.lista[self.con]:  # Español: Compara con elemento actual / English: Compares with current element
                self.aux1 = self.lista[self.con]  # Español: Actualiza valor mayor / English: Updates maximum value
            self.con += 1  # Español: Incrementa contador / English: Increases counter
            if len(self.lista) -1 == self.con:  # Español: Verifica fin de lista / English: Checks end of list
                messagebox.showinfo("El Mayor", f"El mayor es: {self.aux1}")  # Español: Muestra mayor en messagebox / English: Shows maximum in messagebox
                self.con = 0  # Español: Reinicia contador / English: Resets counter
            else:  # Español: Si no llegó al final / English: If not at the end
                return self.mayor()  # Español: Llama recursivamente / English: Calls recursively
            # Español: self.con += 1 / English: self.con += 1
        else:  # Español: Si lista está vacía / English: If list is empty
            messagebox.showerror("Error", "Lista vacia")  # Español: Muestra error / English: Shows error

    # Español: def menor(self,n): / English: def menor(self,n):
    # Español: if self.aux > self.lista[n]  / English: if self.aux > self.lista[n] 

    def menor(self):  # Español: Método para encontrar número menor / English: Method to find minimum number
        if len(self.lista) > 0:  # Español: Verifica si lista no está vacía / English: Checks if list is not empty
            self.aux2 = self.lista[0]  # Español: Inicializa con primer elemento / English: Initializes with first element
            for i in self.lista:  # Español: Recorre cada elemento / English: Iterates through each element
                if self.aux2 > i:  # Español: Compara con elemento actual / English: Compares with current element
                    self.aux2 = i  # Español: Actualiza valor menor / English: Updates minimum value
            messagebox.showinfo("El Menor",f"El menor es {self.aux2}")  # Español: Muestra menor en messagebox / English: Shows minimum in messagebox
        else:  # Español: Si lista está vacía / English: If list is empty
            messagebox.showerror("Error", "Lista vacia")  # Español: Muestra error / English: Shows error


    
    def agregar(self):  # Español: Método para agregar números / English: Method to add numbers
        try:  # Español: Bloque try para manejar errores / English: Try block for error handling
            # Español: self.a = int(self.n1.get()) / English: self.a = int(self.n1.get())
            self.a = random.randint(1,100)  # Español: Genera número aleatorio entre 1-100 / English: Generates random number between 1-100
            self.lista.append(self.a)  # Español: Agrega a lista / English: Adds to list
            self.listview.insert((self.listview.size() + 1),self.a)  # Español: Inserta en Listbox / English: Inserts in Listbox
            # Español: self.n1.delete(0,END) / English: self.n1.delete(0,END)
            # Español: self.b = int(self.n2.get()) / English: self.b = int(self.n2.get())
            # Español: self.lista.append(self.b) / English: self.lista.append(self.b)
            # Español: self.listview.insert((self.listview.size() + 1),self.b) / English: self.listview.insert((self.listview.size() + 1),self.b)
            # Español: self.n2.delete(0,END) / English: self.n2.delete(0,END)

            self.listaElem.config(text=f"La lista: {self.lista}")  # Español: Actualiza label con lista / English: Updates label with list
            self.aux1 = self.lista[0]  # Español: Inicializa variable mayor / English: Initializes maximum variable
            self.listview.insert(self.a)  # Español: Inserta número en Listbox / English: Inserts number in Listbox


            # Español: print(self.lista) / English: print(self.lista)

        except ValueError:  # Español: Captura error de conversión / English: Catches conversion error
             messagebox.showerror("Error", "Algun dato no es numero")  # Español: Muestra error / English: Shows error


if __name__ == "__main__":  # Español: Si es archivo principal / English: If main file
    app = Principal()  # Español: Crea instancia de Principal / English: Creates Main instance
    app.inicio()  # Español: Llama método inicio / English: Calls start method