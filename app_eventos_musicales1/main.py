import tkinter as tk
from models.evento import Evento
from views.vista_inicio import VistaInicio
from views.vista_eventos import VistaEventos
from views.vista_info import VistaInfo
from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_eventos import ControladorEventos
from controllers.controlador_info import ControladorInfo


class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("TOURS DE MUSICA ")
        self.geometry("330x400")
        self.resizable(False, False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        eventos = Evento.cargar_de_json("data/eventos.json")

        controlador_inicio = ControladorInicio(self)
        controlador_eventos = ControladorEventos(self, eventos)
        controlador_info = ControladorInfo(self)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_eventos = VistaEventos(self, controlador_eventos)
        self.vista_info = VistaInfo(self, controlador_info)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_eventos)
        self.ajustar_frame(self.vista_info)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
