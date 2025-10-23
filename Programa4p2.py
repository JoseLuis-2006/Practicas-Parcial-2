from tkinter import *  # Español: Importa todos los módulos de tkinter / English: Imports all tkinter modules
from tkinter import messagebox  # Español: Importa el módulo de cuadros de mensaje / English: Imports message boxes module

class Ventana():  # Español: Define la clase Ventana / English: Defines the Window class
    def __init__(self):  # Español: Método constructor / English: Constructor method
        self.ven = Tk()  # Español: Crea la ventana principal / English: Creates main window
        self.ven.title('Programa 1 con ventanas')  # Español: Establece título ventana / English: Sets window title
        self.ven.geometry('400x200')  # Español: Define tamaño ventana / English: Defines window size
        self.inicio()  # Español: Llama método inicio / English: Calls start method

    def inicio(self):  # Español: Método para interfaz gráfica / English: Method for GUI interface
        Label(self.ven, text='Usuario').pack(pady=10)  # Español: Crea etiqueta usuario / English: Creates user label
        self.us = Entry(self.ven)  # Español: Crea campo entrada usuario / English: Creates user entry field
        self.us.pack(pady=3)  # Español: Empaqueta campo usuario / English: Packs user field
        Label(self.ven, text='Password').pack(pady=10)  # Español: Crea etiqueta password / English: Creates password label
        self.pas = Entry(self.ven)  # Español: Crea campo entrada password / English: Creates password entry field
        self.pas.pack(pady=3)  # Español: Empaqueta campo password / English: Packs password field
        boton = Button(self.ven, text='Aceptar', command=self.revisar).pack()  # Español: Crea botón aceptar / English: Creates accept button
        self.ven.mainloop()  # Español: Inicia bucle principal / English: Starts main loop

    def revisar(self):  # Español: Método validar credenciales / English: Method to validate credentials
        try:  # Español: Bloque try para manejar errores / English: Try block for error handling
            u = str(self.us.get())  # Español: Obtiene texto usuario / English: Gets user text
            p = str(self.pas.get())  # Español: Obtiene texto password / English: Gets password text
            if u == 'admin' and p == '12345':  # Español: Verifica credenciales / English: Verifies credentials
                messagebox.showinfo('Validacion','Usuario y Contraseña correctos')  # Español: Mensaje éxito / English: Success message
            else:  # Español: Si credenciales incorrectas / English: If credentials incorrect
                messagebox.showerror('Error','Usuario y/o contraseña incorrectos')  # Español: Mensaje error / English: Error message
        except:  # Español: Si ocurre excepción / English: If exception occurs
            messagebox.showerror('Error','Introduce datos')  # Español: Mensaje ingresar datos / English: Enter data message

if __name__=='__main__':  # Español: Si es archivo principal / English: If main file
    app = Ventana()  # Español: Crea instancia de Ventana / English: Creates Window instance