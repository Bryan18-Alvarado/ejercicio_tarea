from medio import Medio
class Pelicula(Medio):
    def __init__(self, titulo, duracion, director):
        super().__init__(titulo, duracion)
        self._director = director

    def reproducir(self):
        print(f"Reproduciendo película: {self._titulo}")
