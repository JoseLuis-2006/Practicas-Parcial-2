from Validaciones import validacion  # Español: Importa la clase 'validacion' del módulo 'Validaciones' / English: Imports the 'validacion' class from the 'Validaciones' module
val = validacion()  # Español: Crea una instancia de la clase 'validacion' / English: Creates an instance of the 'validacion' class

class Principal():  # Español: Define una clase llamada 'Principal' / English: Defines a class called 'Principal'
    def __init__(self):  # Español: Constructor de la clase, se ejecuta al crear un objeto / English: Class constructor, runs when an object is created
        self.lista = []  # Español: Crea una lista vacía para guardar las calificaciones / English: Creates an empty list to store grades
        self.num = 0  # Español: Inicializa el contador de calificaciones en 0 / English: Initializes the grade counter to 0
        self.a = ""  # Español: Inicializa una variable vacía para almacenar la calificación temporal / English: Initializes an empty variable to store the temporary grade

    def inicio(self):  # Español: Define el método 'inicio' que controla el flujo del programa / English: Defines the 'inicio' method that controls the program flow
        self.a = input('Escribe una calificacion \n')  # Español: Solicita al usuario que escriba una calificación / English: Asks the user to enter a grade
        if val.ValidarNumeros(self.a):  # Español: Verifica si el valor ingresado es un número válido / English: Checks if the entered value is a valid number
            self.num += 1  # Español: Aumenta el contador de calificaciones en 1 / English: Increases the grade counter by 1
            self.lista.append(int(self.a))  # Español: Convierte la calificación a entero y la agrega a la lista / English: Converts the grade to integer and adds it to the list
            if self.num >= 5:  # Español: Si ya se han ingresado 5 o más calificaciones... / English: If 5 or more grades have been entered...
                print(self.lista)  # Español: Muestra la lista de calificaciones / English: Prints the list of grades
                print(f'El promedio es: {val.Promedio(self.lista)}')  # Español: Muestra el promedio calculado usando la función 'Promedio' / English: Displays the average using the 'Promedio' function
            else:  # Español: Si aún no se han ingresado 5 calificaciones... / English: If fewer than 5 grades have been entered...
                self.inicio()  # Español: Llama de nuevo al método 'inicio' (recursividad) / English: Calls the 'inicio' method again (recursion)
        else:  # Español: Si el valor ingresado no es un número válido... / English: If the entered value is not a valid number...
            print('No es un numero')  # Español: Muestra un mensaje de error / English: Displays an error message
            self.inicio()  # Español: Llama nuevamente al método para volver a pedir la calificación / English: Calls the method again to ask for the grade again

if __name__=='__main__':  # Español: Verifica si el archivo se ejecuta directamente (no importado) / English: Checks if the file is being run directly (not imported)
    app = Principal()  # Español: Crea una instancia (objeto) de la clase 'Principal' / English: Creates an instance (object) of the 'Principal' class
    app.inicio()  # Español: Llama al método 'inicio' para comenzar la ejecución / English: Calls the 'inicio' method to start execution
