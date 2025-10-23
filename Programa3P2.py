from tkinter import *  # Español: Importa todas las clases y funciones del módulo tkinter / English: Imports all classes and functions from the tkinter module
from tkinter import messagebox  # Español: Importa el módulo messagebox para mostrar cuadros de diálogo / English: Imports the messagebox module to show dialog boxes


def Ventana():  # Español: Define una función llamada 'Ventana' que crea la interfaz gráfica / English: Defines a function called 'Ventana' that creates the graphical interface
    def revisar():  # Español: Define una función interna 'revisar' para validar usuario y contraseña / English: Defines an inner function 'revisar' to validate username and password
        try:  # Español: Intenta ejecutar el bloque de código siguiente / English: Tries to execute the following block of code
            u = str(us.get())  # Español: Obtiene el texto del campo de usuario y lo convierte a cadena / English: Gets the text from the username entry and converts it to string
            p = str(pas.get())  # Español: Obtiene el texto del campo de contraseña y lo convierte a cadena / English: Gets the text from the password entry and converts it to string
            if u == 'admin' and p == '12345':  # Español: Verifica si el usuario y la contraseña son correctos / English: Checks if the username and password are correct
                messagebox.showinfo('Validacion','Usuario y Contraseña correctos')  # Español: Muestra un mensaje de éxito / English: Shows a success message
            else:  # Español: Si los datos no coinciden... / English: If the credentials don’t match...
                messagebox.showerror('Error','Usuario y/o contraseña incorrectos')  # Español: Muestra un mensaje de error / English: Displays an error message
        except:  # Español: Si ocurre algún error al obtener los datos... / English: If an error occurs while retrieving data...
            messagebox.showerror('Error','Introduce datos')  # Español: Muestra un mensaje indicando que se deben ingresar datos / English: Displays a message asking to input data

    ven = Tk()  # Español: Crea la ventana principal de la aplicación / English: Creates the main application window
    ven.title('Programa 1 con ventanas')  # Español: Establece el título de la ventana / English: Sets the window title
    ven.geometry('400x200')  # Español: Define el tamaño de la ventana (ancho x alto) / English: Sets the window size (width x height)

    #label = Label(ven, text='Hola Mundo')  # Español: Ejemplo comentado de etiqueta simple / English: Commented example of a simple label
    #label.pack()  # Español: Coloca la etiqueta en la ventana / English: Places the label in the window

    Label(ven, text='Usuario').pack(pady=10)  # Español: Crea y muestra una etiqueta "Usuario" con separación vertical / English: Creates and displays a "User" label with vertical padding
    us = Entry(ven)  # Español: Crea el campo de texto para ingresar el usuario / English: Creates the text entry for the username
    us.pack(pady=3)  # Español: Muestra el campo de usuario en la ventana / English: Displays the username field in the window
    Label(ven, text='Password').pack(pady=10)  # Español: Crea y muestra una etiqueta "Password" con separación vertical / English: Creates and displays a "Password" label with vertical padding
    pas = Entry(ven)  # Español: Crea el campo de texto para la contraseña / English: Creates the text entry for the password
    pas.pack(pady=3)  # Español: Muestra el campo de contraseña en la ventana / English: Displays the password field in the window
    boton = Button(ven, text='Aceptar', command=revisar).pack()  # Español: Crea un botón que ejecuta 'revisar' al presionarlo / English: Creates a button that runs 'revisar' when clicked

    ven.mainloop()  # Español: Mantiene la ventana abierta y en ejecución / English: Keeps the window open and running


if __name__=='__main__':  # Español: Verifica si el archivo se ejecuta directamente / English: Checks if the file is being run directly
    Ventana()  # Español: Llama a la función 'Ventana' para mostrar la interfaz gráfica / English: Calls the 'Ventana' function to display the GUI
