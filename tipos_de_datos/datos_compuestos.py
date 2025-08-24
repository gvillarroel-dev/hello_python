"""
Tipos de datos compuestos -> son colecciones que pueden almacenar múltiples valores
    - Listas (list) -> son iterables (colecciones) donde se puede guardar cualquier tipo de dato y modificar su contenido
    - Tuplas (tuple) -> iterables inmutables donde se pueden guardar datos que no deben modificarse, ya que una vez creadas no pueden modificarse
    - Conjuntos (set) -> son colecciones donde se pueden almacenar cualquier tipo de datos, siempre que estos no se repitan (en caso de duplicación, uno de ellos se omite)
    - Diccionarios (dict) -> son iterables ordenados en formato de par clave-valor, en donde las claves por únicas y con ellas se leen sus datos
"""

"""
LISTAS -> colecciones ordenadas y modificables que pueden contener elementos de cualquier tipo de dato
    - Definidas usando []
    - Los elementos almacenados mantienen un orden específico
    - Cada elemento tiene una posición (índice) comenzando desde 0
    - Puede modificarse, agregar o eliminar elementos
    - Pueden almacenar elementos duplicados

List comprehensions -> forma elegante y resumida de crear listas
    Ejemplo: cuadrados = [x ** 2 for x in range(10)] -> crea una lista llamada "cuadrados" con los cuadrados del 0 al 10

Métodos comunes:
    De agregado_
    - append(item) -> agrega un elemento al final de la lista
    - insert(posición, item) -> agrega un elemento en una posición determinada
    - extend([item, item]) -> extiende los elementos de una lista con otra
    De eliminación_
    - remove(item) -> elimina la primera aparición del elemento indicado
    - pop() -> elimina y retorna el último elemento
    - pop(indice) -> elimina y retorna el elemento en el índice indicado
    - del lista[index] -> palabra reservada que elimina el elemento en el indice determinado
    - clear() -> vacía la lista completamente
    De búsqueda y conteo_
    - index(item) -> retorna el indice de la primera aparición del elemento
    - count(item) -> cuenta las apariciones del elemento indicado
    - in -> palabra reservada que verifica si un elemento se encuentra en una lista
    De ordenamiento_
    - sort() -> ordena la lista original de forma ascendente
    - sort(reverse=True) -> ordena la lista original de forma descendente
    - sorted(lista_original) -> constructor que crea una nueva lista ordenada

"""

# ejemplos de listas
numeros = [1, 2, 3, 4, 5]
otros_numeros = [2, 4, 6, 7, 2, 8, 1, 2, 9, 0.2]
nombres = ["Kigura", "Ugetsu", "Mamiya"]
mix = [1, "texto", 2.4, True]
lista_vacia = []

# Acceso a elementos
print(nombres[0])  # primer elemento
print(nombres[-1])  # último elemento

# rebanadas -> slicing
print(nombres[0:2])
print(nombres[:2])
print(nombres[1:])

# =======================================================================
#                               Métodos más importantes
# =======================================================================

# agregar elementos
lista_vacia.append("Hola, Mundo")
print(lista_vacia)

lista_vacia.insert(0, 32)
print(lista_vacia)

lista_vacia.extend([22, 3.14])
print(lista_vacia)

# eliminar elementos
print(f"\nLista original: {numeros}")

numeros.remove(2)
print(numeros)

print(numeros.pop())
print(numeros.pop(0))

del numeros[1]
print(numeros)

numeros.clear()
print(numeros)

# búsqueda y conteo
print(f"\nBúsqueda y conteo en lista: {otros_numeros}")
print(f"El número 1 está en el índice: {otros_numeros.index(1)}")
print(f"El número 2 aparece {otros_numeros.count(2)} veces")
print(3 in otros_numeros)
print(7 in otros_numeros)

# ordenamiento
print(f"\nLista original: {otros_numeros}")
otros_numeros.sort()
print(f"Lista después de sort(): {otros_numeros}")
otros_numeros.sort(reverse=True)
print(f"Lista después de sort(reverse=True): {otros_numeros}")

# para mantener la lista original:
ordenada = sorted(otros_numeros)
print(ordenada)

# =======================================================================
#                               Operaciones con listas
# =======================================================================

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

print("\nOperaciones básicas con listas")

# concatenación
print(lista_1 + lista_2)

# repetición
print(lista_1 * 3)

# longitud
print(len(lista_1))

# suma, máximo y mínimo (para listas numéricas)
numeros = [1, 2, 3, 4, 5]
print(sum(numeros))
print(max(numeros))
print(min(numeros))

# =======================================================================
#                               Comprehension de listas
# =======================================================================

# forma tradicional:
cuadrados = []
for x in range(10):
    cuadrados.append(x ** 2)

print(cuadrados)

cuadrados.clear()
print(cuadrados)

# con list comprehension
cuadrados = [x ** 2 for x in range(10)]
print(cuadrados)

# Comprehension con condición
pares = [x for x in range(10) if x % 2 == 0]
print(pares)

# otro ejemplo con listas de strings
palabras = ["hola", "mundo", "Python"]
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)


"""
TUPLAS -> colecciones ordenadas e inmutables que pueden contener elementos de cualquier tipo de dato
    - Los elementos mantienen un orden específico
    - Cada elemento tiene una posición (index) comenzando desde 0
    - Los elementos no pueden modificarse, agregarse o eliminarse después de crearse
    - Pueden usarse como claves en diccionarios
    - Permiten elementos duplicados

    Métodos:
    - count(item) -> cuenta las apariciones del elemento indicado en la tupla
    - index(item) -> encuentra el índice de la primera aparición del elemento

    Usos:
    - Para datos que NO deben cambiar
    - Para coordenadas o puntos
    - Para retornar múltiples valores de una función
    - Para configuraciones que no deben cambiar
    - Como claves de diccionarios
        Ejemplo:
        ```
        coordenadas_valor = {
            (0, 0): "origen",
            (1, 1): "diagonal",
            (10, 20): "punto_a"
        }
        ```

"""
print("\n=========== Ejercicio con Tuplas ===========")
frutas = ("manzana", "banana", "toronja")

# acceso por índice
print(frutas[0])
print(frutas[-1])

# slicing 
print(frutas[0:2])
print(frutas[:2])
print(frutas[1:])

# =======================================================================
#                               Métodos de tuplas
# =======================================================================

# Las tuplas solo tienen dos métodos -> por inmutabilidad
numeros = (1, 2, 3, 2, 4, 2)

print(numeros.count(2))
print(numeros.index(2))


# =======================================================================
#                               Operaciones comunes
# =======================================================================
tupla_1 = (1, 2, 3)
tupla_2 = (4, 5, 6)

# concatenación
nueva_tupla = tupla_1 + tupla_2
print(f"Concatenación: {nueva_tupla}")

# repetición
tupla_repetida = tupla_2 * 3
print(f"Repetición: {tupla_repetida}")

# longitud
print(len(tupla_repetida))

# verificar pertenencia
print(2 in tupla_1)

# suma, máximo y mínimo (solo tuplas numéricas)
print(sum(nueva_tupla))
print(max(nueva_tupla))
print(min(nueva_tupla))


# =======================================================================
#                               Creación de tuplas
# =======================================================================

# tradicional
coordenadas = (10, 20)

# Empaquetado de tupla
punto = 10, 20, 30

# tupla de un elemento -> requiere coma
single = (42, )

# tupla vacía
vacia = ()

# convertir tupla desde lista
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla)


# =======================================================================
#                               Desempaquetado
# =======================================================================

# básico
x, y = coordenadas
print(x)
print(y)

# desempaquetado múltiple
persona = ("Allan", 32, "Ingeniero")
nombre, edad, profesion = persona
print(f"Nombre: {nombre}, Edad: {edad}, Profesión: {profesion}")

# intercambio de variables
x, y = y, x
print(f"X = {x} | Y = {y}")

# desempaquetado con *
primero, *medio, ultimo = numeros
print(f"Primero: {primero}, Medio: {medio}, Último: {ultimo}")


# =======================================================================
#                               Tuplas anidadas
# =======================================================================

matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"\n{matriz[0]}")
print(matriz[-1])

# iterción sobre tupla anidada
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print() # nueva línea


# Ejemplo 1: Colores RGB
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

def mezclar_colores(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return ((r1 + r2) // 2, (g1 + g2) // 2, (b1 + b2) // 2)

print(mezclar_colores(VERDE, AZUL))

# Ejemplo 2: Base de datos simple
empleados = [
    ("Kafka", "Ventas", 50000),
    ("Hikaru", "IT", 75000),
    ("Hiromu", "RRHH", 60000)
]

for nombre, departamento, salario in empleados:
    print(f"{nombre} trabaja en {departamento} y gana ${salario}")