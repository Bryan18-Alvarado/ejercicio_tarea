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
