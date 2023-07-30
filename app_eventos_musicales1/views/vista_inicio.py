import tkinter as tk
from tkinter.font import Font


class VistaInicio(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de inicio.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Define una fuente grande y en negrita para el título
        titulo_font = Font(size=24, weight="bold")

        # Crea una etiqueta para el título y la agrega a la vista
        self.titulo = tk.Label(self, text="Bienvenidos!!", font=titulo_font)
        self.titulo.grid(row=0, column=0, pady=5)

        # Define una fuente más pequeña para la descripción de la funcionalidad
        descripcion_font = Font(size=10)

        # Crea una etiqueta para la descripción de la funcionalidad y la agrega a la vista
        self.descripcion = tk.Label(
            self,
            text="Selecciona tus eventos musicales favoritos! Toda la información esta aquí.",
            font=descripcion_font,
            wraplength=300,
        )
        self.descripcion.grid(row=1, column=0, pady=50)

        # Crea el botón para ir a juegos y lo agrega a la vista
        self.boton_eventos = tk.Button(
            self, text="Ir a Eventos", command=self.controlador.mostrar_eventos
        )
        self.boton_eventos.grid(row=2, column=0, pady=10)
        
        # Crea el botón para busqueda
        self.boton_eventos = tk.Button(
            self, text="Busqueda", command=self.controlador.mostrar_eventos #cambiar
        )
        self.boton_eventos.grid(row=3, column=0, pady=10)
        
        # Crea el botón para indice
        self.boton_eventos = tk.Button(
            self, text="Indice", command=self.controlador.mostrar_eventos #cambiar
        )
        self.boton_eventos.grid(row=4, column=0, pady=10)
        
        
