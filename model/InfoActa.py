"""
Contiene la clase InfoActa e
internamente tiene sus respectivos atributos.
Asignatura: POO
"""


class InfoActa:

    # Constructor
    def __init__(self, criterios) -> None:
        super().__init__()

        # Datos del acta
        self.jurado1_checkbox = ""
        self.jurado2_checkbox = ""
        self.autor = ""
        self.fecha_acta = ""
        self.nombre_trabajo = ""
        self.fecha_presentacion = ""
        self.tipo_trabajo = ""
        self.director = ""
        self.codirector = " "
        self.jurado1 = ""
        self.jurado2 = ""
        self.nota_final = 0.0
        self.criterios = criterios
        self.estado = False
