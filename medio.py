class Medio:
    _num_medios = 0

    def __init__(self, titulo, duracion):
        self._titulo = titulo
        self._duracion = duracion
        Medio._num_medios += 1

    @property # permite controlar el acceso y la modificación de los atributos de una clase.
    def titulo(self):
        return self._titulo

    @classmethod  #es un decorador en Python que se utiliza para definir un método de clase
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

#nuevo modulo con herencia
class Pelicula(Medio):
    def __init__(self, titulo, duracion, director):
        super().__init__(titulo, duracion)
        self._director = director

    def reproducir(self):
        print(f"Reproduciendo película: {self._titulo}")


class Cancion(Medio):
    def __init__(self, titulo, duracion, artista):
        super().__init__(titulo, duracion)
        self._artista = artista
        print(f"Número total de medios: {Medio.num_medios()}")

    def reproducir(self):
        print(f"Reproduciendo canción: {self._titulo}")

#nueva clase
class Biblioteca:
    def __init__(self):
        self._medios = []

    def agregar_medio(self, medio):
        self._medios.append(medio)

    def reproducir_todo(self):
        for medio in self._medios:
            medio.reproducir()

    def filtrar_por_categoria(self, categoria):
        return [medio for medio in self._medios if medio.get_categoria() == categoria]


biblioteca = Biblioteca()
pelicula = Pelicula("El Padrino", "2h30m", "Francis Ford Coppola")
cancion = Cancion("Bohemian Rhapsody", "5m55s", "Queen")
pelicula.set_categoria("Aventura")
cancion.set_categoria("Rock")

biblioteca.agregar_medio(pelicula)
biblioteca.agregar_medio(cancion)
medios_rock = biblioteca.filtrar_por_categoria("Rock")
biblioteca.reproducir_todo()
for medio in medios_rock:
    medio.reproducir()
