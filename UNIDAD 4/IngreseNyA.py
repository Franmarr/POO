from tkinter import *
from tkinter import ttk

class Aplicacion():
    def __init__(self):
        root=Tk()
        root.title("Juego de memoria")
        MiFrame=Frame(root,width='500', height='400', bg='blue')
        MiFrame.pack()#esto lo que hace es guardar ese frame dentro de root(raiz).

        nombreEntry=Entry(MiFrame)
        nombreEntry.grid(row=0,column=1, padx=10, pady=10)

        nombreLabel=Label(MiFrame, text="Nombre:")
        nombreLabel.grid(row=0,column=0, padx=10, pady=10,sticky='w')

        apellidoEntry=Entry(MiFrame)
        apellidoEntry.grid(row=1, column=1, padx=10, pady=10)

        apellidoLabel=Label(MiFrame,text="Apellido:")
        apellidoLabel.grid(row=1,column=0, padx=10, pady=10,sticky='w')



        root.mainloop()

if __name__=='__main__':
    miApp=Aplicacion()