class Validar():  # Español: Define la clase Validar / English: Defines the Validate class
    def __init__(self):  # Español: Método constructor / English: Constructor method
        self.index = 0  # Español: Inicializa variable índice / English: Initializes index variable

    def ValidarAscii(self, valor):  # Español: Método para validar usando ASCII / English: Method to validate using ASCII
        con = 0  # Español: Contador para números / English: Counter for numbers
        con2 = 0  # Español: Contador para letras / English: Counter for letters
        for i in valor:  # Español: Recorre cada carácter del valor / English: Iterates through each character of value
            if ord(i) >= 48 and ord(i)<= 57:  # Español: Verifica si es número (0-9) / English: Checks if it's a number (0-9)
                con += 1  # Español: Incrementa contador números / English: Increases number counter
            if (ord(i)>= 65 and ord(i)<=90) or (ord(i)>= 97 and ord(i)<=122):  # Español: Verifica si es letra (A-Z o a-z) / English: Checks if it's a letter (A-Z or a-z)
                con2 += 1  # Español: Incrementa contador letras / English: Increases letter counter

        if con == len(valor):  # Español: Si todos son números / English: If all are numbers
            return "Numeros"  # Español: Retorna "Números" / English: Returns "Numbers"
        elif con2 == len(valor):  # Español: Si todos son letras / English: If all are letters
            return "Letras"  # Español: Retorna "Letras" / English: Returns "Letters"
        else:  # Español: Si es mezcla / English: If it's a mix
            return "Letras y numeros"  # Español: Retorna "Letras y números" / English: Returns "Letters and numbers"


    def ValidarConError(self, valor):  # Español: Método para validar con manejo de errores / English: Method to validate with error handling
        a = 0  # Español: Variable para entero / English: Variable for integer
        b = 0.0  # Español: Variable para float / English: Variable for float
        try:  # Español: Intenta convertir a entero / English: Tries to convert to integer
            a = int(valor)  # Español: Conversión a entero / English: Conversion to integer
            return "numeros"  # Español: Retorna "números" / English: Returns "numbers"
        except ValueError:  # Español: Si falla conversión a entero / English: If integer conversion fails
            try:  # Español: Intenta convertir a float / English: Tries to convert to float
                b = float(valor)  # Español: Conversión a float / English: Conversion to float
                return "Es numero real o con decimales"  # Español: Retorna mensaje decimal / English: Returns decimal message
            except ValueError:  # Español: Si falla conversión a float / English: If float conversion fails
                return "letras o numeros"  # Español: Retorna mensaje texto / English: Returns text message
            
    def ValidarConString(self, valor):  # Español: Método para validar correo recursivamente / English: Method to validate email recursively
        print(valor)  # Español: Imprime el valor / English: Prints the value
        if self.index < len(valor):  # Español: Si no se ha recorrido todo el string / English: If not all string has been traversed
            if valor[self.index] == '@':  # Español: Si encuentra el símbolo @ / English: If it finds @ symbol
                self.index = 0  # Español: Reinicia índice / English: Resets index
                return "se es un correo"  # Español: Retorna que es correo / English: Returns it's an email
            else:  # Español: Si no encuentra @ / English: If @ not found
                if self.index < len(valor):  # Español: Verifica límite del string / English: Checks string limit
                    self.index += 1  # Español: Incrementa índice / English: Increases index
                    return self.ValidarConString(valor)  # Español: Llama recursivamente / English: Calls recursively
                else:  # Español: Si llegó al final / English: If reached the end
                    self.index = 0  # Español: Reinicia índice / English: Resets index
                    return "no es un correo"  # Español: Retorna que no es correo / English: Returns it's not an email
        else:  # Español: Si índice supera longitud / English: If index exceeds length
            self.index = 0  # Español: Reinicia índice / English: Resets index
            return "no es un correo"  # Español: Retorna que no es correo / English: Returns it's not an email
        
        # Español: Comentario método alternativo / English: Comment alternative method
        # if "@" in valor:
        #     return "si es un correo"
        # else:
        #     return "no es in correo"