from tkinter import *  # Español: Importa todos los módulos de tkinter / English: Imports all tkinter modules
from tkinter import messagebox  # Español: Importa el módulo de cuadros de mensaje / English: Imports message boxes module
from validarrepaso import Validar  # Español: Importa la clase Validar / English: Imports Validar class


class Principal():  # Español: Define la clase Principal / English: Defines the Main class
    def __init__(self):  # Español: Método constructor / English: Constructor method
        self.ventana = Tk()  # Español: Crea la ventana principal / English: Creates main window
        self.ventana.geometry("400x200")  # Español: Define tamaño ventana / English: Defines window size
        self.lista = []  # Español: Crea lista vacía / English: Creates empty list
        self.valid = Validar()  # Español: Crea instancia de Validar / English: Creates Validar instance
        

    def inicio(self):  # Español: Método para interfaz gráfica / English: Method for GUI interface
        Label(self.ventana, text="Programa de python con TKInter").place(x=100, y=20)  # Español: x = columna y= fila / English: x = column y= row
        Label(self.ventana, text="Escribe un dato").place(x=50, y=50)  # Español: Label para entrada dato / English: Label for data entry
        self.dato = Entry(self.ventana)  # Español: Campo entrada de datos / English: Data entry field
        self.dato.place(x=150, y=50, width=150)  # Español: Posiciona campo entrada / English: Positions entry field
        Button(self.ventana, text="Validar", command=self.ValidarDatos).place(x=150, y=90, width=150)  # Español: Botón validar / English: Validate button
        self.mostrar = Label(self.ventana, text="ejemplo")  # Español: Label para mostrar resultados / English: Label to show results
        self.mostrar.place(x=20, y=150)  # Español: Posiciona label mostrar / English: Positions show label
        self.ventana.mainloop()  # Español: Inicia bucle principal / English: Starts main loop

    def ValidarDatos(self):  # Español: Método para validar datos / English: Method to validate data
        val = self.dato.get()  # Español: Obtiene texto del campo / English: Gets text from field
        if val != "":  # Español: Verifica que no esté vacío / English: Checks it's not empty
            self.Revisar(val)  # Español: Llama método Revisar / English: Calls Revisar method
            self.lista.append(val)  # Español: Agrega valor a lista / English: Adds value to list
            self.dato.delete(0,END)  # Español: Limpia campo entrada / English: Clears entry field
            # print(self.lista)  # Español: Comentario imprimir lista / English: Comment print list
            self.mostrar.config(text=f'{self.lista}')  # Español: Actualiza label con lista / English: Updates label with list
            # respuesta = self.valid.ValidarAscii(val)  # Español: Comentario validar ASCII / English: Comment validate ASCII
            # respuesta = self.valid.ValidarConError(val)  # Español: Comentario validar con error / English: Comment validate with error
            respuesta = self.valid.ValidarConString(val)  # Español: Llama validación con string / English: Calls string validation
            messagebox.showinfo("Validar Datos", f'El dato es {respuesta}')  # Español: Muestra resultado / English: Shows result
        else:  # Español: Si campo está vacío / English: If field is empty
            messagebox.showerror("Error","Caja de texto esta vacia")  # Español: Muestra error / English: Shows error

    def Revisar(self, v):  # Español: Método para revisar valor / English: Method to check value
        print(v)  # Español: Imprime valor en consola / English: Prints value in console


if __name__=='__main__':  # Español: Si es archivo principal / English: If main file
    app = Principal()  # Español: Crea instancia de Principal / English: Creates Main instance
    app.inicio()  # Español: Llama método inicio / English: Calls start method