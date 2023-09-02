class Medio:
    _num_medios = 0



    def __init__(self, titulo, duracion):
        self._titulo = titulo
        self._duracion = duracion
        Medio._num_medios += 1



    @property
    def titulo(self):
        return self._titulo


    @classmethod
    def num_medios(cls):
        return cls._num_medios


    def get_titulo(self):
        return self._titulo


    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo


    def get_duracion(self):
        return self._duracion

    def set_duracion(self, nueva_duracion):
        self._duracion = nueva_duracion

    def reproducir(self):
        print(f"Reproduciendo {self._titulo}")

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_categoria(self):
        return self._categoria
