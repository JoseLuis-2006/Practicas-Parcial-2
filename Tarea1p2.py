# hacer un programa que lea nombre y 3 calificaciomes
# que se agregaran con las siguientes restricciones
# las calificaciones se agregaran en orden descedente,
# una vez realizado esto mostrara una pregunta si deseas otra persona
# si la respuesta es si, la primer lista se agregara a otra lista que
# contenga los 4 datos, para agregar a otra persona.

from tkinter import * 
from tkinter import messagebox

def ventana():
    def mostrar():
        messagebox.showinfo('Lista Final', lista2)
        print(lista2)

    def revisar():
        
        try:
            lista1 = []
            n = (nom.get())
            c1 = int(cal1.get())
            c2 = int(cal2.get())
            c3 = int(cal3.get())

            if (c1 > c2):
                if(c1 > c3):
                    lista1.append(n)
                    lista1.append(c1)
                    if (c2 > c3):
                        messagebox.showinfo('Calificaciones',f'es mayor {c1}\nes el de en medio {c2}\nes el menor {c3}')
                        lista1.append(c2)
                        lista1.append(c3)
                        lista2.append(lista1)
                    else:
                        messagebox.showinfo('Calificaciones',f'es mayor {c1}\nes el de en medio {c3}\nes el menor {c2}')
                        lista1.append(c3)
                        lista1.append(c2)
                        lista2.append(lista1)
                else:
                    messagebox.showinfo('Calificaciones',f'es el de en medio {c1}\nes mayor {c3}\nes el menor {c2}')
                    lista1.append(n)
                    lista1.append(c3)
                    lista1.append(c1)
                    lista1.append(c2)
                    lista2.append(lista1)
            else:
                if (c2 > c3):
                    lista1.append(n)
                    lista1.append(c2)
                    if (c1>c3):
                        messagebox.showinfo('Calificaciones',f'es mayor {c2}\nes el de en medio {c1}\nes el menor {c3}')
                        lista1.append(c1)
                        lista1.append(c3)
                        lista2.append(lista1)
                    else:
                        messagebox.showinfo('Calificaciones',f'es mayor {c2}\nes el de en medio {c3}\nes el menor {c1}')
                        lista1.append(c3)
                        lista1.append(c1)
                        lista2.append(lista1)
                else:
                    messagebox.showinfo('Calificaciones',f'es el de en medio {c2}\nes mayor {c3}\nes el menor {c1}')
                    lista1.append(n)
                    lista1.append(c3)
                    lista1.append(c2)
                    lista1.append(c1)
                    lista2.append(lista1)
            if len(lista2) == 1:
                boton2.pack(pady=20)
            
        except:
            messagebox.showerror('Error','Introduce datos')

        nom.delete(0,END)
        cal1.delete(0,END)
        cal2.delete(0,END)
        cal3.delete(0,END)
            
        

    ven = Tk()
    ven.title('Programa 1 con ventanas')
    ven.geometry('500x500')

    Label(ven, text='Escribe un nombre').pack(pady=10)
    nom = Entry(ven)
    nom.pack(pady=3)
    Label(ven, text='Escribe una calificacion').pack(pady=10)
    cal1 = Entry(ven)
    cal1.pack(pady=3)
    Label(ven, text='Escribe una calificacion').pack(pady=10)
    cal2 = Entry(ven)
    cal2.pack(pady=3)
    Label(ven, text='Escribe una calificacion').pack(pady=10)
    cal3 = Entry(ven)
    cal3.pack(pady=3)

    boton = Button(ven, text='Confirmar', command=revisar).pack()
    boton2 = Button(ven, text='Mostrar lista', command=mostrar)
    ven.mainloop()
    


lista2 = []
if __name__=='__main__':
   ventana()