from cancion import Cancion
from peliculas import Pelicula
from biblioteca import Biblioteca

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
