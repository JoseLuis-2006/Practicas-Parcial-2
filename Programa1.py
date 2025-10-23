def inicio(num):  # Español: Se define una función llamada 'inicio' que recibe un parámetro 'num' / English: Defines a function called 'inicio' that takes a parameter 'num'
    a = int(input('Escribe una calificacion \n'))  # Español: Pide al usuario una calificación y la convierte a entero / English: Asks the user for a grade and converts it to an integer
    num += 1  # Español: Incrementa el valor de 'num' en 1 / English: Increases the value of 'num' by 1
    lista.append(a)  # Español: Agrega la calificación a la lista 'lista' / English: Adds the grade to the list 'lista'
    if num >= 5:  # Español: Si se han ingresado 5 o más calificaciones... / English: If 5 or more grades have been entered...
        print(lista)  # Español: Muestra la lista completa de calificaciones / English: Prints the complete list of grades
    else:  # Español: Si aún no se han ingresado 5 calificaciones... / English: If fewer than 5 grades have been entered...
        return inicio(num)  # Español: Llama de nuevo a la función (recursividad) / English: Calls the function again (recursion)

lista = []  # Español: Crea una lista vacía para guardar las calificaciones / English: Creates an empty list to store the grades
global num  # Español: Declara la variable 'num' como global (no es realmente necesario) / English: Declares 'num' as global (not really needed)
num = 0  # Español: Inicializa 'num' con 0 / English: Initializes 'num' with 0

if __name__ == '__main__':  # Español: Verifica si el archivo se ejecuta directamente / English: Checks if the file is being run directly
    inicio(num)  # Español: Llama a la función 'inicio' para empezar / English: Calls the 'inicio' function to start
