import os
import random
from typing import List, Tuple
from readchar import readkey, key
from functools import reduce
class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = self.convertir(mapa)
        self.inicio = inicio
        self.fin = fin
        self.nombre = ""
    def convertir(self, maze_generator: str) -> List[List[str]]:
        filas = maze_generator.strip().split('\n')
        laberinto = list(map(list, filas))
        return laberinto
    def mostrar_laberinto(self):
        for fila in self.mapa:
            print("".join(fila))
    def limpiar_mostrar(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for fila in self.mapa:
            print(''.join(fila))
    def main_loop(self):
        px, py = self.inicio
        while (px, py) != self.fin:
            if 0 <= px < len(self.mapa[0]) and 0 <= py < len(self.mapa):
                self.mapa[py][px] = 'P'
            self.limpiar_mostrar()
            print(px, py)
            teclado = readkey()
            px_nueva, py_nueva = px, py
            if teclado == key.UP and py > 0 and self.mapa[py - 1][px] != '#':
                py_nueva -= 1
            elif teclado == key.DOWN and py < len(self.mapa) - 1 and self.mapa[py + 1][px] != '#':
                py_nueva += 1
            elif teclado == key.LEFT and px > 0 and self.mapa[py][px - 1] != '#':
                px_nueva -= 1
            elif teclado == key.RIGHT and px < len(self.mapa[0]) - 1 and self.mapa[py][px + 1] != '#':
                px_nueva += 1
            if 0 <= px_nueva < len(self.mapa[0]) and 0 <= py_nueva < len(self.mapa):
                self.mapa[py][px] = ' '
                px, py = px_nueva, py_nueva
            self.mapa[py][px] = 'P'
            self.limpiar_mostrar()
        print(f"Felicidades {self.nombre} lo has logrado")
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
if __name__ == "__main__":
    # Uso de la clase Juego
    map_generator = """..###################
    ........#.#.#.#...#.#
    #.#.###.#.#.#.#.#.#.#
    #.#.#.....#.....#.#.#
    #.###.#####.###.###.#
    #.#.#.......#.......#
    #.#.#####.#######.#.#
    #.....#...#...#...#.#
    #.###.###.###.###.###
    #.#...#.......#.....#
    #####.#####.#########
    #.#.#.....#...#.#...#
    #.#.#.#####.#.#.###.#
    #.......#...#...#...#
    ###.###.###########.#
    #...#.#.#.....#...#.#
    #.###.#####.#####.#.#
    #...................#
    ###.#.#####.#####.#.#
    #...#...#...#.....#.#
    ###################.#"""
    end = (19, 20)
    inicio = (0, 0)
    juego = Juego(map_generator, inicio, end)
    juego.nombre = "Jugador 1"
    juego.mostrar_laberinto()
    juego.main_loop()
    # Uso de la clase JuegoArchivo
    path_a_mapas = "map1.txt", "map2.txt"
    juego_archivo = JuegoArchivo(path_a_mapas)
    juego_archivo.mostrar_laberinto()
    juego_archivo.main_loop()