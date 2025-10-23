# hacer un programa que lea nombre y 3 calificaciomes
# que se agregaran con las siguientes restricciones
# las calificaciones se agregaran en orden descedente,
# una vez realizado esto mostrara una pregunta si deseas otra persona
# si la respuesta es si, la primer lista se agregara a otra lista que
# contenga los 4 datos, para agregar a otra persona.

from tkinter import *  # Español: Importa todos los módulos de tkinter / English: Imports all tkinter modules
from tkinter import messagebox  # Español: Importa el módulo de cuadros de mensaje / English: Imports message boxes module

def ventana():  # Español: Define función ventana / English: Defines window function
    def mostrar():  # Español: Función para mostrar lista final / English: Function to show final list
        messagebox.showinfo('Lista Final', lista2)  # Español: Muestra lista en messagebox / English: Shows list in messagebox
        print(lista2)  # Español: Imprime lista en consola / English: Prints list in console

    def revisar():  # Español: Función para revisar y ordenar calificaciones / English: Function to check and sort grades
        
        try:  # Español: Bloque try para manejar errores / English: Try block for error handling
            lista1 = []  # Español: Lista temporal para cada estudiante / English: Temporary list for each student
            n = (nom.get())  # Español: Obtiene nombre del campo / English: Gets name from field
            c1 = int(cal1.get())  # Español: Obtiene y convierte calificación 1 / English: Gets and converts grade 1
            c2 = int(cal2.get())  # Español: Obtiene y convierte calificación 2 / English: Gets and converts grade 2
            c3 = int(cal3.get())  # Español: Obtiene y convierte calificación 3 / English: Gets and converts grade 3

            if (c1 > c2):  # Español: Compara calificación 1 y 2 / English: Compares grade 1 and 2
                if(c1 > c3):  # Español: Si calificación 1 es mayor que 3 / English: If grade 1 is greater than 3
                    lista1.append(n)  # Español: Agrega nombre a lista / English: Adds name to list
                    lista1.append(c1)  # Español: Agrega calificación 1 / English: Adds grade 1
                    if (c2 > c3):  # Español: Compara calificación 2 y 3 / English: Compares grade 2 and 3
                        messagebox.showinfo('Calificaciones',f'es mayor {c1}\nes el de en medio {c2}\nes el menor {c3}')  # Español: Muestra orden / English: Shows order
                        lista1.append(c2)  # Español: Agrega calificación 2 / English: Adds grade 2
                        lista1.append(c3)  # Español: Agrega calificación 3 / English: Adds grade 3
                        lista2.append(lista1)  # Español: Agrega lista1 a lista2 / English: Adds lista1 to lista2
                    else:  # Español: Si calificación 3 es mayor que 2 / English: If grade 3 is greater than 2
                        messagebox.showinfo('Calificaciones',f'es mayor {c1}\nes el de en medio {c3}\nes el menor {c2}')  # Español: Muestra orden / English: Shows order
                        lista1.append(c3)  # Español: Agrega calificación 3 / English: Adds grade 3
                        lista1.append(c2)  # Español: Agrega calificación 2 / English: Adds grade 2
                        lista2.append(lista1)  # Español: Agrega lista1 a lista2 / English: Adds lista1 to lista2
                else:  # Español: Si calificación 3 es mayor que 1 / English: If grade 3 is greater than 1
                    messagebox.showinfo('Calificaciones',f'es el de en medio {c1}\nes mayor {c3}\nes el menor {c2}')  # Español: Muestra orden / English: Shows order
                    lista1.append(n)  # Español: Agrega nombre a lista / English: Adds name to list
                    lista1.append(c3)  # Español: Agrega calificación 3 / English: Adds grade 3
                    lista1.append(c1)  # Español: Agrega calificación 1 / English: Adds grade 1
                    lista1.append(c2)  # Español: Agrega calificación 2 / English: Adds grade 2
                    lista2.append(lista1)  # Español: Agrega lista1 a lista2 / English: Adds lista1 to lista2
            else:  # Español: Si calificación 2 es mayor que 1 / English: If grade 2 is greater than 1
                if (c2 > c3):  # Español: Si calificación 2 es mayor que 3 / English: If grade 2 is greater than 3
                    lista1.append(n)  # Español: Agrega nombre a lista / English: Adds name to list
                    lista1.append(c2)  # Español: Agrega calificación 2 / English: Adds grade 2
                    if (c1>c3):  # Español: Compara calificación 1 y 3 / English: Compares grade 1 and 3
                        messagebox.showinfo('Calificaciones',f'es mayor {c2}\nes el de en medio {c1}\nes el menor {c3}')  # Español: Muestra orden / English: Shows order
                        lista1.append(c1)  # Español: Agrega calificación 1 / English: Adds grade 1
                        lista1.append(c3)  # Español: Agrega calificación 3 / English: Adds grade 3
                        lista2.append(lista1)  # Español: Agrega lista1 a lista2 / English: Adds lista1 to lista2
                    else:  # Español: Si calificación 3 es mayor que 1 / English: If grade 3 is greater than 1
                        messagebox.showinfo('Calificaciones',f'es mayor {c2}\nes el de en medio {c3}\nes el menor {c1}')  # Español: Muestra orden / English: Shows order
                        lista1.append(c3)  # Español: Agrega calificación 3 / English: Adds grade 3
                        lista1.append(c1)  # Español: Agrega calificación 1 / English: Adds grade 1
                        lista2.append(lista1)  # Español: Agrega lista1 a lista2 / English: Adds lista1 to lista2
                else:  # Español: Si calificación 3 es mayor que 2 / English: If grade 3 is greater than 2
                    messagebox.showinfo('Calificaciones',f'es el de en medio {c2}\nes mayor {c3}\nes el menor {c1}')  # Español: Muestra orden / English: Shows order
                    lista1.append(n)  # Español: Agrega nombre a lista / English: Adds name to list
                    lista1.append(c3)  # Español: Agrega calificación 3 / English: Adds grade 3
                    lista1.append(c2)  # Español: Agrega calificación 2 / English: Adds grade 2
                    lista1.append(c1)  # Español: Agrega calificación 1 / English: Adds grade 1
                    lista2.append(lista1)  # Español: Agrega lista1 a lista2 / English: Adds lista1 to lista2
            if len(lista2) == 1:  # Español: Si hay al menos un estudiante / English: If there's at least one student
                boton2.pack(pady=20)  # Español: Muestra botón mostrar lista / English: Shows show list button
            
        except:  # Español: Captura cualquier error / English: Catches any error
            messagebox.showerror('Error','Introduce datos')  # Español: Muestra error / English: Shows error

        nom.delete(0,END)  # Español: Limpia campo nombre / English: Clears name field
        cal1.delete(0,END)  # Español: Limpia campo calificación 1 / English: Clears grade 1 field
        cal2.delete(0,END)  # Español: Limpia campo calificación 2 / English: Clears grade 2 field
        cal3.delete(0,END)  # Español: Limpia campo calificación 3 / English: Clears grade 3 field
            
        

    ven = Tk()  # Español: Crea ventana principal / English: Creates main window
    ven.title('Programa 1 con ventanas')  # Español: Establece título ventana / English: Sets window title
    ven.geometry('500x500')  # Español: Define tamaño ventana / English: Defines window size

    Label(ven, text='Escribe un nombre').pack(pady=10)  # Español: Label para nombre / English: Label for name
    nom = Entry(ven)  # Español: Campo entrada nombre / English: Name entry field
    nom.pack(pady=3)  # Español: Empaqueta campo nombre / English: Packs name field
    Label(ven, text='Escribe una calificacion').pack(pady=10)  # Español: Label para calificación 1 / English: Label for grade 1
    cal1 = Entry(ven)  # Español: Campo entrada calificación 1 / English: Grade 1 entry field
    cal1.pack(pady=3)  # Español: Empaqueta campo calificación 1 / English: Packs grade 1 field
    Label(ven, text='Escribe una calificacion').pack(pady=10)  # Español: Label para calificación 2 / English: Label for grade 2
    cal2 = Entry(ven)  # Español: Campo entrada calificación 2 / English: Grade 2 entry field
    cal2.pack(pady=3)  # Español: Empaqueta campo calificación 2 / English: Packs grade 2 field
    Label(ven, text='Escribe una calificacion').pack(pady=10)  # Español: Label para calificación 3 / English: Label for grade 3
    cal3 = Entry(ven)  # Español: Campo entrada calificación 3 / English: Grade 3 entry field
    cal3.pack(pady=3)  # Español: Empaqueta campo calificación 3 / English: Packs grade 3 field

    boton = Button(ven, text='Confirmar', command=revisar).pack()  # Español: Botón confirmar / English: Confirm button
    boton2 = Button(ven, text='Mostrar lista', command=mostrar)  # Español: Botón mostrar lista / English: Show list button
    ven.mainloop()  # Español: Inicia bucle principal / English: Starts main loop
    


lista2 = []  # Español: Lista global para todos los estudiantes / English: Global list for all students
if __name__=='__main__':  # Español: Si es archivo principal / English: If main file
   ventana()  # Español: Llama función ventana / English: Calls window function