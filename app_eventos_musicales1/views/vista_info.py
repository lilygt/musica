import tkinter as tk


class VistaInfo(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la información de un evento.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        self.evento_label = tk.Label(self, text="")
        self.evento_label.pack(pady=50)
        self.evento_label.config(justify=tk.LEFT)
        self.boton_regresar = tk.Button(
            self,
            text="Regresar a la lista de eventos musicales",
            command=self.controlador.regresar_evento,
        )
        self.boton_regresar.pack(pady=10)

    def mostrar_info_evento(self, evento):
        """
        Muestra la información del evento recibido como parámetro.
        """
        info = f"Nombre: {evento.nombre}\nArtista: {evento.artista}\nGenero: {evento.genero}\nid_ubicacion: {evento.id_ubicacion}\nHora Inicio: {evento.hora_inicio}\nHora Fin: {evento.hora_fin}\nDescripcion: {evento.descripcion}\nImagen: {evento.imagen}\n"
        self.evento_label["text"] = info

        