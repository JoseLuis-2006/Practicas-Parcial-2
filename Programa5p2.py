from tkinter import *  # Español: Importa todos los módulos de tkinter / English: Imports all tkinter modules
from tkinter import messagebox  # Español: Importa el módulo de cuadros de mensaje / English: Imports message boxes module

class Principal():  # Español: Define la clase Principal / English: Defines the Main class
    def __init__(self):  # Español: Método constructor / English: Constructor method
        self.ven = Tk()  # Español: Crea la ventana principal / English: Creates main window
        self.ven.title('Programa 5 con ventanas')  # Español: Establece título ventana / English: Sets window title
        self.ven.geometry('450x250')  # Español: Define tamaño ventana / English: Defines window size
        self.lista = []  # Español: Crea lista vacía para promedios / English: Creates empty list for averages
        self.inicio()  # Español: Llama método inicio / English: Calls start method

    def sumar(self):  # Español: Método para sumar elementos / English: Method to sum elements
        s = 0  # Español: Inicializa contador en 0 / English: Initializes counter at 0
        for i in self.lista:  # Español: Recorre cada elemento en lista / English: Iterates through each list element
            s += 1  # Español: Incrementa contador en 1 / English: Increases counter by 1
        return s  # Español: Retorna la suma / English: Returns the sum

    def promediar(self):  # Español: Método para calcular promedio / English: Method to calculate average
        try:  # Español: Bloque try para manejar errores / English: Try block for error handling
            a = float(self.n1.get())  # Español: Convierte primer número a float / English: Converts first number to float
            b = float(self.n2.get())  # Español: Convierte segundo número a float / English: Converts second number to float
            c = float(self.n3.get())  # Español: Convierte tercer número a float / English: Converts third number to float
            d = float(self.n4.get())  # Español: Convierte cuarto número a float / English: Converts fourth number to float
            pro = (a+b+c+d)/4  # Español: Calcula promedio de 4 números / English: Calculates average of 4 numbers
            self.l6.config(text=str(pro))  # Español: Actualiza label con promedio / English: Updates label with average
            self.lista.append(pro)  # Español: Agrega promedio a la lista / English: Adds average to the list
            self.l7.config(text=str(self.lista))  # Español: Muestra lista de promedios / English: Shows averages list
            self.n1.delete(0,END)  # Español: Limpia campo número 1 / English: Clears number 1 field
            self.n2.delete(0,END)  # Español: Limpia campo número 2 / English: Clears number 2 field
            self.n3.delete(0,END)  # Español: Limpia campo número 3 / English: Clears number 3 field
            self.n4.delete(0,END)  # Español: Limpia campo número 4 / English: Clears number 4 field
            suma = self.sumar()  # Español: Obtiene suma de elementos / English: Gets sum of elements
            p = suma / len(self.lista)  # Español: Calcula promedio general / English: Calculates general average
            self.l8.config(text=f'Promedio General: {str(p)}')  # Español: Muestra promedio general / English: Shows general average

        except ValueError:  # Español: Captura error de conversión / English: Catches conversion error
            messagebox.showerror("Error","Algun dato no es numero")  # Español: Mensaje error / English: Error message
            self.n1.delete(0,END)  # Español: Limpia campo número 1 / English: Clears number 1 field
            self.n2.delete(0,END)  # Español: Limpia campo número 2 / English: Clears number 2 field
            self.n3.delete(0,END)  # Español: Limpia campo número 3 / English: Clears number 3 field
            self.n4.delete(0,END)  # Español: Limpia campo número 4 / English: Clears number 4 field

    def salir(self):  # Español: Método para cerrar ventana / English: Method to close window
        self.ven.destroy()  # Español: Destruye la ventana / English: Destroys the window

    def inicio(self):  # Español: Método para interfaz gráfica / English: Method for GUI interface
        l1 = Label(self.ven, text="Escribe un numero").place(y=10,x=20)  # Español: Label número 1 / English: Number 1 label
        l2 = Label(self.ven, text="Escribe un numero").place(y=50,x=20)  # Español: Label número 2 / English: Number 2 label
        l3 = Label(self.ven, text="Escribe un numero").place(y=90,x=20)  # Español: Label número 3 / English: Number 3 label
        l4 = Label(self.ven, text="Escribe un numero").place(y=130,x=20)  # Español: Label número 4 / English: Number 4 label
        self.n1 = Entry(self.ven)  # Español: Campo entrada número 1 / English: Number 1 entry field
        self.n1.place(y=10,x=130)  # Español: Posiciona campo 1 / English: Positions field 1
        self.n2 = Entry(self.ven)  # Español: Campo entrada número 2 / English: Number 2 entry field
        self.n2.place(y=50,x=130)  # Español: Posiciona campo 2 / English: Positions field 2
        self.n3 = Entry(self.ven)  # Español: Campo entrada número 3 / English: Number 3 entry field
        self.n3.place(y=90,x=130)  # Español: Posiciona campo 3 / English: Positions field 3
        self.n4 = Entry(self.ven)  # Español: Campo entrada número 4 / English: Number 4 entry field
        self.n4.place(y=130,x=130)  # Español: Posiciona campo 4 / English: Positions field 4

        l5 = Label(self.ven, text="Promedio:").place(y=150,x=130)  # Español: Label promedio / English: Average label
        self.l6 = Label(self.ven,text="0.0")  # Español: Label para mostrar promedio / English: Label to show average
        self.l6.place(y=150,x=200)  # Español: Posiciona label promedio / English: Positions average label
        b1 = Button(self.ven, text="Promedio", command=self.promediar).place(y=50,x=300)  # Español: Botón calcular / English: Calculate button
        b2 = Button(self.ven, text="Salir", command=self.salir).place(y=90,x=300)  # Español: Botón salir / English: Exit button
        self.l7 = Label(self.ven,text="[]")  # Español: Label para lista promedios / English: Label for averages list
        self.l7.place(y=170,x=200)  # Español: Posiciona label lista / English: Positions list label
        self.l8 = Label(self.ven,text="Promedio general: 0.0")  # Español: Label promedio general / English: General average label
        self.l8.place(y=190,x=150)  # Español: Posiciona label promedio general / English: Positions general average label

        self.ven.mainloop()  # Español: Inicia bucle principal / English: Starts main loop

if __name__=='__main__':  # Español: Si es archivo principal / English: If main file
    app = Principal()  # Español: Crea instancia de Principal / English: Creates Main instance