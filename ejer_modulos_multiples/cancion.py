from medio import Medio


class Cancion(Medio):
    def __init__(self, titulo, duracion, artista):
        super().__init__(titulo, duracion)
        self._artista = artista
        print(f"Número total de medios: {Medio.num_medios()}")

    def reproducir(self):
        print(f"Reproduciendo canción: {self._titulo}")
