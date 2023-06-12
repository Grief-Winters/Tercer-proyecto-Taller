from agenda import agenda as Agenda, lista as Lista
from datetime import datetime
from typing import Self, Optional
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
    def imprimir_lista(self,nodo):
        self._imprimir_lista(self)
    def _imprimir_lista(self,lista: Lista) -> None:
        list=[]
        nodo = lista
        while nodo:
            list.append(nodo)
            nodo = nodo.sig
        return(list)
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
    app.geometry("850x700")
    app.title("Tercer proyecto programado")
    miAgenda= MiAgenda
    miPersona=MiPersona(None,None,None)
    miApartado=MiApartado
    miPunto=MiPunto
    miDiscusion=MiDiscusion

    #Tabs
    tabview = customtkinter.CTkTabview(master=app,height=500,width=500)
    tabview.pack()
    tabview.add("Agenda") 
    tabview.add("Participantes") 
    tabview.add("Apartados")  
    tabview.add("Puntos")  
    tabview.add("Discusiones") 
    tabview.place_configure(relx=0.2,rely=0.005,height=700, width=750)

    #funciones de la interfaz
    def button_function1():
        global miAgenda
        dialog = customtkinter.CTkInputDialog(text="Titulo de la agenda:", title="Agenda")
        text = dialog.get_input()  # waits for input
        miAgenda=MiAgenda(fecha=datetime.today(),titulo=text)
        textbox_agenda = customtkinter.CTkTextbox(master=tabview.tab("Agenda"), width=400, corner_radius=0)
        textbox_agenda.insert("0.0",miAgenda.titulo )
        textbox_agenda.configure(state="disabled")  
        textbox_agenda.pack(padx=50, pady=100)
    def button_function2():
        pass
    def button_function3():#BOTON para añadir un participante
        dialog = customtkinter.CTkInputDialog(text="Nombre:", title="Participante")
        text1 = dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Apellido 1:", title="Participante")
        text2 = dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Apellido 2:", title="Participante")
        text3 = dialog.get_input()
        miPersona.agregar(MiPersona(text1.capitalize(), text2.capitalize(), text3.capitalize()))
        textbox_participantes = customtkinter.CTkTextbox(master=tabview.tab("Participantes"), width=400, corner_radius=0)
        textbox_participantes.insert("0.0", "{0}".format(miPersona.imprimir_lista(miPersona)))
        textbox_participantes.configure(state="disabled")
        textbox_participantes.pack(padx=50, pady=100)
    def button_function4():
        dialog = customtkinter.CTkInputDialog(text="Nombre:", title="Apartado")
        text1 = dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Descripcion:", title="Apartado")
        text2 = dialog.get_input()
        miApartado.agregar(text1.capitalize,text2.capitalize)
        textbox = customtkinter.CTkTextbox(master=tabview.tab("Apartados"), width=400, corner_radius=0)
        textbox.insert("0.0","{0}".format(miAgenda.participantes._asList))
        textbox.configure(state="disabled")  
        textbox.pack(padx=50, pady=100)

    #Botones
    button_Agenda = customtkinter.CTkButton(master=app, text="Crear la agenda", command=button_function1)
    button_Agenda.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)
    button2 = customtkinter.CTkButton(master=app, text="holder", command=button_function2)
    button2.place(relx=0.1, rely=0.9, anchor=tkinter.CENTER)
    button_Participantes = customtkinter.CTkButton(master=tabview.tab("Participantes"), text="Agregar participante", command=button_function3)
    button_Participantes.configure(width=80, height=30)
    button_Participantes.place(relx=0.85, rely=0.1, anchor=tkinter.CENTER)
    button_apartados = customtkinter.CTkButton(master=tabview.tab("Apartados"), text="Agregar Apartado", command=button_function4)
    button_apartados.configure(width=80, height=30)
    button_apartados.place(relx=0.85, rely=0.1, anchor=tkinter.CENTER)
    button_tab = customtkinter.CTkButton(master=tabview.tab("Puntos"), text="button tab 2")
    button_tab.place(relx=0.7)

    app.mainloop()
inter()
pass

