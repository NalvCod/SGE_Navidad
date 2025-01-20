import random

'''
Escribe una función llamada imprimir_arbol que reciba un número entero n y dibuje
un árbol de Navidad en la consola con n niveles.
'''

def imprimir_arbol(n):
    for i in range(1, n + 1):
        espacios = " " * (n - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)

    base = " " * (n - 2) + "|||"
    print(base)

print('\nEJERCICIO 1')
imprimir_arbol(7)
print('\n------------------------')

'''
Crea una función llamada filtrar_regalos que reciba una lista de regalos como una
tupla y filtre los que empiezan con la letra "R". Devuelve una nueva lista con solo esos
regalos.
'''
def filtrar_regalos(regalos):
    regalosR = [regalo for regalo in regalos if regalo.lower().startswith('r')]
    return regalosR

print('\nEJERCICIO 2')
regalos = ("Ramo", "Ropa", "Consola", "Libro", "Perro", "Robot")
resultados = filtrar_regalos(regalos)
print(resultados)
print('\n------------------------')

'''
Tienes una lista de números que representan el tamaño de bolas de nieve que hiciste.
Crea una función llamada contar_bolas que reciba la lista y cuente cuántas bolas son
mayores o iguales a 5.
'''
def contar_bolas(numeros):
    contador = 0

    for numero in numeros:
        if numero >= 5:
            contador = contador+1

    return contador

print('\nEJERCICIO 3')
print(contar_bolas([1, 5, 3, 10]))
print('\n------------------------')

'''
Crea una función llamada sorteo_navidad que reciba dos listas: una con nombres de
personas y otra con los premios. El sorteo asignará aleatoriamente un premio a cada
persona y devolverá una lista de tuplas con los resultados.
'''

def sorteo_navidad(listaNombres, listaPremios):
    premios_random = random.sample(listaPremios, len(listaNombres))
    resultados = []

    for i in range(len(listaNombres)):
        resultados.append((listaNombres[i], premios_random[i]))

    return resultados

nombres = ["Nahuel", "Luis", "Sara", "Laura"]
premios = ["Switch", "Ordenador", "Pijama", "Calcetines", "test"]

resultados = sorteo_navidad(nombres, premios)
print('\nEJERCICIO 4')
print(resultados)
print('\n------------------------')

'''
Crea una función llamada cuenta_regresiva que reciba un número n y haga una
cuenta regresiva desde ese número hasta 1. Por cada número, imprime "3" si es
divisible por 3, "?" si es divisible por 5, y "^" si es divisible por ambos.
'''
def cuenta_regresiva(n):
    for i in range(n, 0, -1):
        linea = str(i)
        if i%3 == 0 and i % 5 == 0:
            linea += " divisible por 3 y 5"
        elif i%3 == 0:
            linea += " divisible por 3"
        elif i%5 == 0:
            linea += " divisible por 5"
        print(linea)

print('\nEJERCICIO 5')
cuenta_regresiva(10)
print('\n------------------------')

'''
Escribe una función llamada sec_natal que reciba una lista de tuplas con el nombre de
una persona y su edad, y devuelva una lista con el nombre de las personas mayores de
edad (18 años o más). La lista debe estar ordenada de forma alfabética.
'''

def sec_natal(listaNombreEdad):
    listaMayoresEdad = []

    for nombres in listaNombreEdad:
        if nombres[1] >= 18:
            listaMayoresEdad.append(nombres[0])

    listaMayoresEdad.sort()
    return listaMayoresEdad

print('\nEJERCICIO 6')
personas = [("Nahuel", 25), ("Luis", 22),("Bebe", 2), ("Sara", 24), ("Laura", 26)]
resultado = sec_natal(personas)
print(resultado)
print('\n------------------------')

'''
Crea una función llamada resolver_sudoku que reciba una lista de listas representando
un tablero de Sudoku incompleto, con ceros (0) representando las casillas vacías. La
función debe intentar resolver el Sudoku, devolviendo el tablero resuelto. Si no es
posible resolver el Sudoku con los valores proporcionados, la función debe devolver
None. El Sudoku debe respetar las reglas:
1. Cada fila debe contener los números del 1 al 9 sin repetirse.
2. Cada columna debe contener los números del 1 al 9 sin repetirse.
3. Cada una de las 9 subcuadrículas de 3x3 debe contener los números del 1 al 9
sin repetirse.
Entrada -> Salida
'''

def crearTablero():
    tablero = [[0 for _ in range(9)] for _ in range(9)]

    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print(*fila)

print("\nEjercicio SUDOKU")
tablero = crearTablero()
imprimir_tablero(tablero)
print('\n------------------------')

'''
El problema de las N-Reinas consiste en colocar N reinas en un tablero de
ajedrez de ( N x N ) de manera que ninguna reina ataque a otra. Esto significa
que no puede haber dos reinas en la misma fila, columna o diagonal.
Crea una función resolver_n_reinas(n) que encuentre una solución al problema
para un tablero de tamaño n. La función debe devolver una lista de posiciones
(tuplas) donde se colocan las reinas.
'''

def ejercicio_reinas(n):
    tablero = [-1] * n

    def esValido(fila, col):
        for i in range(fila):
            if tablero[i] == col or abs(tablero[i] - col) == abs(i - fila):
                return False
        return True

    def colocarReinas(fila):
        if fila == n:
            return True

        for col in range(n):
            if esValido(fila, col):
                tablero[fila] = col
                if colocarReinas(fila + 1):
                    return True
                tablero[fila] = -1
        return False

    colocarReinas(0)

    solucion = [(i, tablero[i]) for i in range(n)]
    return solucion

def mostrar_tablero(n, solucion):
    tablero = [['[]' for _ in range(n)] for _ in range(n)]

    for fila, col in solucion:
        tablero[fila][col] = 'R'

    for fila in tablero:
        print(" ".join(fila))

print("\nEjercicio REINAS")
solucion = ejercicio_reinas(10)
mostrar_tablero(10, solucion)
print(f'COORDENADAS {solucion}')
print('\n------------------------')

'''
• Cada letra del mensaje se convierte en un número según su posición en
el abecedario (A=1, B=2, ..., Z=26, ignorando mayúsculas y minúsculas).
• Los números del mensaje cifrado se agrupan en bloques de tamaño k.
• Cada bloque se suma para generar un número único por bloque.
• Si un bloque tiene menos de k números (es el último bloque), se calcula
solo con los números que contiene.
Escribe un programa que contenga las siguientes funciones:
• cifrar_mensaje(mensaje: str, k: int) -> list[int]: Recibe el mensaje original y
el tamaño del bloque k y devuelve una lista de enteros con los valores
cifrados de cada bloque.
• descifrar_mensaje(cifrado: list[int], k: int) -> str: Recibe la lista cifrada y el
tamaño del bloque k, y reconstruye el mensaje original.
Además:
• Ignora cualquier carácter que no sea una letra (como espacios, números
o signos de puntuación).
• Devuelve el mensaje cifrado como una lista de números y el descifrado
como texto.
'''

def cifrar_mensaje(mensaje: str, k: int) -> list[int]:
    mensaje = mensaje.lower()
    numeros = []

    for letra in mensaje:
        if letra >= 'a' and letra <= 'z':
            numero = ord(letra) - ord('a') + 1
            numeros.append(numero)

    bloqueCifrados = []
    for i in range(0, len(numeros), k):
        bloque = numeros[i:i + k]
        bloqueCifrados.append(sum(bloque))

    return bloqueCifrados
print('\nEJERCICIO CIFRADO')
mensaje = 'Me llamo Nahuel'
cifrado = cifrar_mensaje(mensaje, 2)
print(f'Mensaje cifrado: {cifrado}')
print('\n------------------------')