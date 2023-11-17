def convertir(self, maze_generator: str) -> List[List[str]]:
    filas = maze_generator.strip().split('\n')
    laberinto = list(map(list, filas))
    return laberinto

# uso de la función map