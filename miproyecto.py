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
    """
    Arg:
    """
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("850x700")
    app.title("Tercer proyecto programado")
    miAgenda= MiAgenda(None,None)

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
        textbox = customtkinter.CTkTextbox(master=tabview.tab("Agenda"), width=400, corner_radius=0)
        textbox.insert("0.0",miAgenda.titulo )
        textbox.configure(state="disabled")  
        textbox.pack(padx=50, pady=100)
    def button_function2():
        pass
    def button_function3():
        dialog = customtkinter.CTkInputDialog(text="Nombre:", title="Participante")
        text1 = dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Apellido 1:", title="Participante")
        text2 = dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Apellido 2:", title="Participante")
        text3 = dialog.get_input()
        miAgenda.agregar_participante(text1.capitalize,text2.capitalize,text3.capitalize)
        textbox = customtkinter.CTkTextbox(master=tabview.tab("Participantes"), width=400, corner_radius=0)
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
    button_tab = customtkinter.CTkButton(master=tabview.tab("Puntos"), text="button tab 2")
    button_tab.place(relx=0.7)

    app.mainloop()
inter()
pass

