class validacion():  # Español: Define la clase validacion / English: Defines the validation class
    def __init__(self):  # Español: Método constructor / English: Constructor method
        self.suma = 0  # Español: Inicializa variable suma / English: Initializes sum variable
        self.promedio = 0.0  # Español: Inicializa variable promedio / English: Initializes average variable

    def ValidarNumeros(self, valor):  # Español: Método para validar números / English: Method to validate numbers
        if valor.isdigit():  # Español: Verifica si el valor son solo dígitos / English: Checks if value contains only digits
            return True  # Español: Retorna verdadero si es número / English: Returns true if it's a number
        else:  # Español: Si no son solo dígitos / English: If not only digits
            return False  # Español: Retorna falso / English: Returns false
        
    def Promedio(self, lista):  # Español: Método para calcular promedio / English: Method to calculate average
        for i in lista:  # Español: Recorre cada elemento de la lista / English: Iterates through each list element
            suma += i  # Español: ERROR: debería ser self.suma / English: ERROR: should be self.suma
        self.promedio = self.suma / len(lista)  # Español: Calcula el promedio / English: Calculates the average
        return self.promedio  # Español: Retorna el promedio / English: Returns the average