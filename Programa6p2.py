from tkinter import *  # Español: Importa todos los módulos de tkinter / English: Imports all tkinter modules
from tkinter import messagebox  # Español: Importa el módulo de cuadros de mensaje / English: Imports message boxes module


class Principal():  # Español: Define la clase Principal / English: Defines the Main class
    def __init__(self):  # Español: Método constructor / English: Constructor method
        self.ven = Tk()  # Español: Crea la ventana principal / English: Creates main window
        self.ven.title('Programa 6 con Ventanas')  # Español: Establece título ventana / English: Sets window title
        self.ven.geometry('450x450')  # Español: Define tamaño ventana / English: Defines window size
        self.a = 0  # Español: Variable para primer número / English: Variable for first number
        self.b = 0  # Español: Variable para segundo número / English: Variable for second number
        self.lista = []  # Español: Lista para almacenar números / English: List to store numbers
        self.aux1 = 0  # Español: Variable auxiliar para mayor / English: Auxiliary variable for maximum
        self.aux2 = 0  # Español: Variable auxiliar para menor / English: Auxiliary variable for minimum
        self.cont = 0  # Español: Contador para recursividad / English: Counter for recursion

    def inicio(self):  # Español: Método para interfaz gráfica / English: Method for GUI interface
        l1 = Label(self.ven, text="Programa 6")  # Español: Crea título principal / English: Creates main title
        l1.grid(row=1, column=2)  # Español: Posiciona título en grid / English: Positions title in grid

        l2 = Label(self.ven, text="Escribe un numero")  # Español: Label para primer número / English: Label for first number
        l2.grid(row=3, column=1, padx=15, pady=10)  # Español: Posiciona label en grid / English: Positions label in grid

        Label(self.ven, text="").grid(row=2, column=2)  # Español: Label vacío para espacio / English: Empty label for spacing

        self.n1 = Entry(self.ven,)  # Español: Campo entrada primer número / English: First number entry field
        self.n1.grid(row=3, column=2)  # Español: Posiciona campo en grid / English: Positions field in grid

        l3 = Label(self.ven, text="Escribe otro numero")  # Español: Label para segundo número / English: Label for second number
        l3.grid(row=5, column=1, padx=5, pady=5)  # Español: Posiciona label en grid / English: Positions label in grid

        Label(self.ven, text="").grid(row=4, column=2)  # Español: Label vacío para espacio / English: Empty label for spacing

        self.n2 = Entry(self.ven,)  # Español: Campo entrada segundo número / English: Second number entry field
        self.n2.grid(row=5, column=2)  # Español: Posiciona campo en grid / English: Positions field in grid

        b1 = Button(self.ven, text="Agregar", command=self.agregar)  # Español: Botón agregar números / English: Add numbers button
        b1.grid(row=6,column=1)  # Español: Posiciona botón agregar / English: Positions add button
        b2 = Button(self.ven, text="Mayor", command=self.mayor)  # Español: Botón encontrar mayor / English: Find maximum button
        b2.grid(row=6,column=2)  # Español: Posiciona botón mayor / English: Positions maximum button
        b3 = Button(self.ven, text="Menor", command=self.menor)  # Español: Botón encontrar menor / English: Find minimum button
        b3.grid(row=6,column=3, padx=10)  # Español: Posiciona botón menor / English: Positions minimum button
        b4 = Button(self.ven, text="Salir", command=self.salir)  # Español: Botón salir / English: Exit button
        b4.grid(row=6,column=4, padx=25)  # Español: Posiciona botón salir / English: Positions exit button
        self.listaElementos = Label(self.ven, text="")  # Español: Label para mostrar lista / English: Label to show list
        self.listaElementos.grid(row=8, column=1, pady=15)  # Español: Posiciona label lista / English: Positions list label
        self.listview = Listbox(self.ven, height=10,  # Español: Crea Listbox para números / English: Creates Listbox for numbers
                                width=15,bg='black',  # Español: Configura color fondo / English: Configures background color
                                activestyle="dotbox", fg="white")  # Español: Configura estilo y color texto / English: Configures style and text color
        self.listview.grid(row=2,column=4)  # Español: Posiciona Listbox / English: Positions Listbox

        self.ven.mainloop()  # Español: Inicia bucle principal / English: Starts main loop

    def mayor(self):  # Español: Método para encontrar número mayor / English: Method to find maximum number
        if len(self.lista) > 0:  # Español: Verifica si lista no está vacía / English: Checks if list is not empty
        ##for i in self.lista:  # Español: Comentario método alternativo / English: Comment alternative method
            if self.aux1 < self.lista[self.cont]:  # Español: Compara con elemento actual / English: Compares with current element
                self.aux1 = self.lista[self.cont]  # Español: Actualiza valor mayor / English: Updates maximum value
            self.cont += 1  # Español: Incrementa contador / English: Increases counter
            if len(self.lista)-1 < self.cont:  # Español: Verifica fin de lista / English: Checks end of list
                print(f'el mayor es {self.aux1}')  # Español: Imprime mayor en consola / English: Prints maximum in console
                messagebox.showinfo('El mayor', {self.aux1})  # Español: Muestra mayor en messagebox / English: Shows maximum in messagebox
                self.cont = 0  # Español: Reinicia contador / English: Resets counter
            else:  # Español: Si no llegó al final / English: If not at the end
                return self.mayor()  # Español: Llama recursivamente / English: Calls recursively
        else:  # Español: Si lista está vacía / English: If list is empty
            print("Lista vacia")  # Español: Imprime mensaje consola / English: Prints console message
            messagebox.showerror("Error","La lista esta vacia")  # Español: Muestra error / English: Shows error

    def menor(self):  # Español: Método para encontrar número menor / English: Method to find minimum number
        if len(self.lista) > 0:  # Español: Verifica si lista no está vacía / English: Checks if list is not empty
            for i in self.lista:  # Español: Recorre cada elemento / English: Iterates through each element
                if self.aux2 > i:  # Español: Compara con elemento actual / English: Compares with current element
                    self.aux2 = i  # Español: Actualiza valor menor / English: Updates minimum value
            print(f'el menor es {self.aux2}')  # Español: Imprime menor en consola / English: Prints minimum in console
            messagebox.showinfo('El menor', {self.aux2})  # Español: Muestra menor en messagebox / English: Shows minimum in messagebox
        else:  # Español: Si lista está vacía / English: If list is empty
            messagebox.showerror("Error","La lista esta vacia")  # Español: Muestra error / English: Shows error


    def agregar(self):  # Español: Método para agregar números / English: Method to add numbers
        try:  # Español: Bloque try para manejar errores / English: Try block for error handling
            self.a = int(self.n1.get())  # Español: Convierte primer número a entero / English: Converts first number to integer
            self.lista.append(self.a)  # Español: Agrega a lista / English: Adds to list
            self.listview.insert(self.listview.size()+1,self.a)  # Español: Inserta en Listbox / English: Inserts in Listbox
            self.n1.delete(0,END)  # Español: Limpia campo número 1 / English: Clears number 1 field
            self.b = int(self.n2.get())  # Español: Convierte segundo número a entero / English: Converts second number to integer
            self.listview.insert(self.listview.size()+1, self.b)  # Español: Inserta en Listbox / English: Inserts in Listbox
            self.lista.append(self.b)  # Español: Agrega a lista / English: Adds to list
            self.n2.delete(0,END)  # Español: Limpia campo número 2 / English: Clears number 2 field
            print(self.lista)  # Español: Imprime lista en consola / English: Prints list in console
            self.aux2 = self.lista[0]  # Español: Inicializa variable menor / English: Initializes minimum variable
            self.listaElementos.config(text=f'{self.lista}')  # Español: Actualiza label con lista / English: Updates label with list
            
        except ValueError:  # Español: Captura error de conversión / English: Catches conversion error
            messagebox.showerror("Error","Algun dato no es numero")  # Español: Muestra error / English: Shows error

    def salir(self):  # Español: Método para cerrar ventana / English: Method to close window
        self.ven.destroy()  # Español: Destruye la ventana / English: Destroys the window



if __name__=='__main__':  # Español: Si es archivo principal / English: If main file
    app = Principal()  # Español: Crea instancia de Principal / English: Creates Main instance
    app.inicio()  # Español: Llama método inicio / English: Calls start method