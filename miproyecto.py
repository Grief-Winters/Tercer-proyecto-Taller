from agenda import agenda as Agenda, lista as Lista, persona as Persona
from datetime import datetime
import tkinter
import customtkinter

# funcionalidades del proyecto
class MiAgenda(Agenda):
    def __init__(self,titulo:str,fecha:datetime) -> None:
        super().__init__()
        self.titulo:str=titulo
        self.fecha:datetime=fecha
        self.participantes:MiPersona

    def agregar_participante(self, nombre: str, apellido1: str, apellido2: str):
        if self.participantes==None:
            self.participantes=MiPersona(nombre=nombre,apellido1=apellido1,apellido2=apellido2)
        else:
            self.participantes.agregar(nombre,apellido1,apellido2)
    @property
    def asDict(self):
        return {"Título":self.titulo,"fecha":self.fecha.__str__(),"participantes":self.participantes.asList}


class MiLista(Lista):
    def __init__(self) -> None:
        super().__init__()
    
    def _agregar(self,r,e):
        if self==None:
            return e
        else:
            self.sig=self._agregar(r.sig,e)

class MiPersona(Persona):
    def __init__(self, nombre: str, apellido1: str, apellido2: str) -> None:
        super().__init__(nombre, apellido1, apellido2)

    def agregar (self,nombre: str, apellido1: str, apellido2: str):
        nueva_persona= MiPersona(nombre,apellido1,apellido2)
        self._agregar(self,nueva_persona)

    def _agregar(self,r,p):
        if r==None:
            return p
        else:
            r.sig=self._agregar(r.sig,p)
    @property
    def asList(self):
        if self==None:
            return []
        else:
            return self._asList(self)
        
    def _asList(self,r):
        r:MiPersona=r
        if r.sig==None:
            return [r.__str__()]
        else:
            return [r.__str__()]+self._asList(r.sig)
    
    def __str__(self) -> str:
        return ("{0} {1} {2}".format(self.nombre,self.apellido1,self.apellido2))

#funcion para crear una interfaz grafica
def inter(): #se usa el ejemplo de CTk como base para la interfaz
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("800x700")
    miAgenda= MiAgenda(None,None)

    #Tabs
    tabview = customtkinter.CTkTabview(master=app,height=500,width=500)
    tabview.pack(padx=50, pady=100)
    tabview.add("Puntos")  # add tab at the end
    tabview.add("Participantes")  # add tab at the end
    def button_function1():
        global miAgenda
        dialog = customtkinter.CTkInputDialog(text="Titulo de la agenda:", title="Agenda")
        text = dialog.get_input()  # waits for input
        miAgenda=MiAgenda(fecha=datetime.today(),titulo=text)
        
    def button_function2():
        textbox = customtkinter.CTkTextbox(app)
        textbox.pack(padx=50, pady=100)
        textbox.insert("0,0", miAgenda.asDict)
        textbox.configure(state="disabled")# configure textbox to be read-only
    def button_function3():
        dialog = customtkinter.CTkInputDialog(text="Nombre:", title="Agenda")
        text1 = dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Apellido 1:", title="Agenda")
        text2 = dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Apellido 2:", title="Agenda")
        text3 = dialog.get_input()
        miAgenda.agregar_participante(text1,text2,text3)
    # Use CTkButton instead of tkinter Button
    button1 = customtkinter.CTkButton(master=app, text="Crear la agenda", command=button_function1)
    button1.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)
    button2 = customtkinter.CTkButton(master=app, text="Imprimir agenda", command=button_function2)
    button2.place(relx=0.1, rely=0.9, anchor=tkinter.CENTER)
    button3 = customtkinter.CTkButton(master=app, text="Agregar participante", command=button_function3)
    button3.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)

    app.mainloop()
inter()
pass

