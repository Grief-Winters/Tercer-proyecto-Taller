from agenda import agenda as Agenda, lista as Lista
from datetime import datetime
from typing import Any, Self, Optional
import tkinter
import customtkinter

# funcionalidades del proyecto
class MiLista(Lista):
    def __init__(self) -> None:
        super().__init__()

    def borrar(self, nodo: Self) -> None:
        self._borrar(self, nodo)

    def _borrar(self, raiz, nodo: Self) -> None:
        if raiz.sig == nodo:
            raiz.sig = nodo.sig
            del nodo
        else:
            self._borrar(raiz.sig, nodo)

    def buscar(self, key) -> Optional[Self]:
        return self._buscar(self, key)

    def _buscar(self, raiz, key):
        if not raiz:
            return
        if key(raiz):
            return raiz
        return self._buscar(raiz.sig, key)

    def agregar(self, nodo:object)->None:
        self._agregar(self,nodo)

    def _agregar(self, raiz:Self, nodo: Self)->None:
        if not raiz.sig:
            raiz.sig = nodo
        else:
            self._agregar(raiz.sig, nodo)

    def imprimir_lista(self, nodo) -> str:
        return (self._imprimir_lista(nodo))

    def _imprimir_lista(self, lista) -> None:
        result = []
        nodo = lista
        while nodo:
            result.append(str(nodo))  # Agregar representación legible del objeto
            print(str(nodo))
            nodo = nodo.sig
        return (result[1:])
class MiAgenda(MiLista):
    def __init__(self,titulo:str,fecha:datetime) -> None:
        super().__init__()
        self.titulo:str=titulo
        self.fecha:datetime=fecha
        self.participantes:MiPersona
        self.apartados:MiApartado

    def __str__(self) -> str:
        return ("Titulo: {0} \n Fecha:{1} \n Participantes: {2}".format(self.titulo,self.fecha,self.participantes))
    
class MiPersona(MiLista):
    def __init__(self, nombre: str, apellido1: str, apellido2: str) -> None:
        super().__init__()
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2



    def __str__(self) -> str:
        return ("{0} {1} {2}".format(self.nombre, self.apellido1, self.apellido2))
    
class MiApartado(MiLista):
    def __init__(self,nombre:str,descripcion:str) -> None:
        super().__init__()
        self.nombre:str=nombre
        self.descripcion:str=descripcion
        self.puntos:MiPunto=None

    def __str__(self) -> str:
        return ("Apartado: {0} \nDescripcion:{1}".format(self.nombre,self.descripcion))
class MiPunto(MiLista):
    def __init__(self,nombre:str,descripcion:str) -> None:
        super().__init__()
        self.nombre:str=nombre
        self.descripcion:str=descripcion
        self.discusiones:MiDiscusion=None
    def __str__(self) -> str:
        return ("Punto: {0} \nDescripcion:{1}".format(self.nombre,self.descripcion))

class MiDiscusion(MiLista):
    def __init__(self,transcripcion:str,participante:str) -> None:
        super().__init__()
        self.transcripcion:str=transcripcion
        self.participante:str=participante

    def __str__(self) -> str:
        return ("Transcripción:{0} \n Participante: {1}".format(self.transcripcion,self.participante))
"""
Discusiones=MiDiscusion("Hola hola", "Asdrubal")
Discusiones.agregar(MiDiscusion("Adios adios","Yuba"))
miPersona=MiPersona("Asdru","ulate","cama")
miPersona.agregar(MiPersona("Asdru","ula","cama"))
def imprimir_lista(lista: Lista) -> None:
    nodo = lista
    while nodo:
        print(nodo)
        nodo = nodo.sig
imprimir_lista(Discusiones)
imprimir_lista(miPersona)
"""

#funcion para crear una interfaz grafica
def inter(): #se usa el ejemplo de CTk como base para la interfaz
    """
    Arg:
    """
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("500x500")
    app.title("Tercer proyecto programado")
    miAgenda= MiAgenda
    miPersona=MiPersona(None,None,None)
    miApartado=MiApartado(None,None)
    miPunto=MiPunto(None,None)
    global miDiscusion
    miDiscusion=MiDiscusion(None,None)

    #funciones de la interfaz
    def button_function1():
        """
        Botón para crear la Agenda
        """
        dialog = customtkinter.CTkInputDialog(text="Titulo de la agenda:", title="Agenda")
        text = dialog.get_input()  # waits for input
        miAgenda=MiAgenda(fecha=datetime.today(),titulo=text)
        miAgenda.agregar(miAgenda)
        label = customtkinter.CTkLabel(app, text="Titulo:{0}\n Hora de creacion:{1}".format(miAgenda.titulo,miAgenda.fecha), fg_color="transparent")
        label.pack(padx=0.4)
    def button_function2():
        """
        Botón para añadir una discusion
        """
        global miDiscusion
        dialog = customtkinter.CTkInputDialog(text="Transcripcion:", title="Transcripcion")
        text1 = dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Nombre del participante:", title="Participante")
        text2 = dialog.get_input()
        if miPersona.buscar(lambda miPersona: miPersona.nombre == text2):
            miDiscusion.agregar(MiDiscusion(text1,text2))
            miDiscusion.imprimir_lista(miDiscusion)
        else:
            dialog = customtkinter.CTkInputDialog(text="El participante no existe", title="ERROR")
   

    def button_function3():
        """
        Botón para añadir un participante
        """
        dialog = customtkinter.CTkInputDialog(text="Nombre:", title="Participante")
        text1 = dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Apellido 1:", title="Participante")
        text2 = dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Apellido 2:", title="Participante")
        text3 = dialog.get_input()
        miPersona.agregar(MiPersona(text1.capitalize(),text2.capitalize(),text3.capitalize()))
        miPersona.imprimir_lista(miPersona) 

    def button_function4():
        """
        Botón para añadir un apartado
        """
        dialog = customtkinter.CTkInputDialog(text="Nombre:", title="Apartado")
        text1 = dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Descripcion:", title="Apartado")
        text2 = dialog.get_input()
        miApartado.agregar(MiApartado(text1.capitalize,text2.capitalize))

    def button_function5():
        """
        Botón para añadir un punto
        """
        dialog = customtkinter.CTkInputDialog(text="Nombre:", title="Apartado")
        text1 = dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Descripcion:", title="Apartado")
        text2 = dialog.get_input()
    def button_function6():
        pass
    #Botones
    button_Agenda = customtkinter.CTkButton(master=app, text="Crear la agenda", command=button_function1)
    button_Agenda.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
    button_discusion = customtkinter.CTkButton(master=app, text="Agregar discusión", command=button_function2)
    button_discusion.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    button_Participantes = customtkinter.CTkButton(master=app, text="Agregar participante", command=button_function3)
    button_Participantes.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    button_apartados = customtkinter.CTkButton(master=app, text="Agregar Apartado", command=button_function4)
    button_apartados.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    button_punto = customtkinter.CTkButton(master=app, text="Agregar Punto",command=button_function5)
    button_punto.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)
    button_HTML = customtkinter.CTkButton(master=app, text="Generar HTML",command=button_function6)
    button_HTML.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)

    app.mainloop()
inter()
pass

