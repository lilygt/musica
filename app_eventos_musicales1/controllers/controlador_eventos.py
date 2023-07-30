class ControladorEventos:
    """clase ControladorEventos: maneja la lógica y la interacción entre la vista y el modelo de eventos."""
    
    def __init__(self, app, modelo_evento):
        self.app = app
        self.modelo_evento = modelo_evento
        
    """Constructor toma dos parámetros: app y modelo_evento. app :instancia principal de la aplicación, -modelo_evento: información sobre los eventos. Almacenados en un JSON"""

    def obtener_eventos(self):
        return self.modelo_evento

    """Este método devuelve la referencia al modelo de eventos (self.modelo_evento). Acceso directo a los datos del modelo desde fuera del controlador."""
    
    def seleccionar_evento(self):
        """
        Obtiene el índice del evento seleccionado y llama a la vista de
        información para mostrar la información del evento.
        """
        indice = self.app.vista_eventos.obtener_evento_seleccionado()
        if indice is not None:
            evento = self.modelo_evento[indice]
            self.app.vista_info.mostrar_info_evento(evento)
            self.app.cambiar_frame(self.app.vista_info)

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
