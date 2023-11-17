class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas: str):
        super().__init__("", (0, 0), (0, 0))
        self.cargar_mapa_aleatorio(path_a_mapas)
    def cargar_mapa_aleatorio(self, path_a_mapas: str):
        lista_archivos = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(lista_archivos)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)
        with open(path_completo, 'r') as archivo:
            lineas = archivo.readlines()
            dimensiones = lineas[0].strip().split(',')
            inicio = tuple(map(int, lineas[1].strip().split(',')))
            fin = tuple(map(int, lineas[2].strip().split(',')))
            mapa = reduce(lambda x, y: x + y, map(str.strip, lineas[3:]))
            self.mapa = self.convertir(mapa)
            self.inicio = inicio
            self.fin = fin
            self.nombre = nombre_archivo.split('.')[0]
# sustitucion de el bucle. Para usar la función reduce