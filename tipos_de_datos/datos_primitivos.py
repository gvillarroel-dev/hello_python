"""
Variables -> contenedores que almacenan datos y a los que se les asigna un nombre para referenciarlos (y recuperar, trabajar y modificar ese dato almacenado)
    - Deben definirse y asignarse al mismo tiempo -> en caso de no tener un valor para inicializar, se coloca 'None' (representa un valor vacío, aún no determinado)
    - Su nombre debe ser descriptivo en formato snake_case
        - No pueden llevar palabras reservadas como nombre
        - No pueden comenzar en mayúsculas (reservadas para clases)
    - De tipado dinámico -> no se necesita declarar el tipo de dato almacenado en la variable
    - Son mutables (reasignables) -> pueden cambiar de valor como de tipo en cualquier momento

=============================================================

TIPOS DE DATOS -> definen qué clase de información puede almacenar una variable y qué operaciones se pueden realizar con ella
    - Numbers -> int, float, complex
    - Strings -> cadenas de caracteres (texto)
    - iterables -> list, tuple, dict, set
    - Booleanos -> True, False
    - None -> valor vacío

Verificación de tipo:
    - type() -> retorna el tipo de dato exacto del objeto pasado como argumento
    - isinstance(variable, tipo) -> verifica si el primer argumento es de un tipo específico (segundo argumento)

Conversión de tipos -> realizado para poder operar con un valor determinado que tiene cierto tipo de dato con el que no se puede operar de forma correcta
    - int() -> convierte a entero
    - float() -> convierte a flotante (número de punto decimal)
    - str() -> convierte a cadena de caracteres

"""

"""
STRING -> secuencias inmutables de caracteres que representan texto plano
    - creados usando comillas simples, dobles o triples
    - inmutables -> una vez creadas no pueden modificarse (las operaciones crean nuevos strings, no modifican el original)
    - se puede acceder a cada caracter de forma individual mediante indexación (comenzando desde 0)
    - permite rebanar porciones del string -> string[0:2]
        - primer número -> inicio de rebanada (incluido)
        - segundo -> fin de rebanada (no incluido)
    - concatenación -> unión entre strings mediante operaciones de suma (+) entre palabras

f-string -> forma de inyectar variables en strings para trabajar con strings dinámicos

    Métodos principales:
    Transformación
        - upper() → convierte string a mayúsculas
        - lower() → convierte string a minúsculas
        - title() → primera letra de cada palabra en mayúscula
        - strip() → elimina espacios al inicio y final del string
        - replace(viejo, nuevo) → reemplaza texto
        - swapcase() → intercambia mayúsculas/minúsculas
    Búsqueda y verificación
        - find(substring) → encuentra la posición de una subcadena
        - count(substring) → cuenta ocurrencias (apariciones) del string o caracter indicado
        - startswith(prefix) → verifica si comienza con cierto texto
        - endswith(suffix) → verifica si termina con cierto texto
        - isdigit() → verifica si contiene solo dígitos
        - isalpha() → verifica si contiene solo letras
        - islower(), isupper(), isdecimal(), isnumeric(), isspace() , etc.
    División y unión
        - split(separador) → divide el string en una lista de caracteres individuales, separado según la aparición del separador
        - join(lista) → une elementos de lista en string
"""

# print() -> función integrada, imprime en consola cualquier dato pasado como argumento pero no almacena su valor
print("Hola mundo")

texto = " Hola Mundo "
nombre = "Fujiwara Hikaru"
email = "hfujiwara@email.com"

print(f"Texto original: {texto}")

# métodos de limpieza
print(f"strip(): '{texto.strip()}'")  # Quita espacios adelante y detrás
print(f"lower(): '{nombre.lower()}'")  # convierte en minúsculas
print(f"upper(): '{nombre.upper()}'")  # convierte en mayúsculas
print(f"title(): '{nombre.title()}'")  # primera letra mayúscula

# métodos de búsqueda
print(f"\nfind('Mundo'): {texto.find('Mundo')}")  # busca la posición de una subcadena en el string aplicado -> retorna -1 si no existe
print(f"count('a'): {nombre.count('a')}")  # cuenta las ocurrencias de una subcadena o patrón indicado
print(f"startswith('Fujiwara'): {nombre.startswith('Fujiwara')}") 
print(f"endswith('.com'): {email.endswith('.com')}")

#métodos de verificación 
print(f"\nisalpha(): {'Hola'.isalpha()}")  # verifica si son solo letras
print(f"isdigit(): {'123'.isdigit()}")    # verifica si son solo dígitos
print(f"isalnum(): {'Hola123'.isalnum()}")  # verifica si son letras y números


# ==================== DIVISIÓN Y UNIÓN ====================
frase = "Python,es,genial,para,programar"
palabras = frase.split(',')
print(f"\nsplit(','): {palabras}")

frase_join = ' '.join(palabras)
print(f"join(' '): '{frase_join}'")

# uso de f-strings para cadenas dinámicas
edad = 25
salario = 3500.50
print(f"Formato: {nombre} tiene {edad} años y gana ${salario:.2f}")  # .2f -> indica que se tomarán 2 decimales luego del punto flotante


# format()
mensaje = "Hola {}, tienes {} años".format("Yuuno", 30)
print(f"format(): {mensaje}")


# # ================================= Ejercicio: crear un programa que pida nombre, edad y altura, y muestre un mensaje personalizado ================================= 
# name = input("Ingrese su nombre: ")
# age = input("Ingrese su edad: ")
# height = input("Ingrese su altura: ")

# print(f"Hola, {name}. Tienes {age} años y tienes una estatura de {height}mts")


# # ================================= EJERCICIO: el usuario debe ingresar una frase y luego debe poder modificar una palabra específica ================================= 
# sentence = input("Ingrese su frase: ")
# print(f"Su frase es: {sentence}")
# word_1 = input("Ingrese la palabra a reemplazar: ")
# word_2 = input("Ingrese la palabra que reemplazará la palabra anterior: ")
# print(sentence.replace(word_1, word_2))



"""
Números -> 3 tipos:
    - int -> representan todos los números sin parte decimal (incluye positivos, negativos y cero)
        - tienen precisión arbitraria (no hay límite de tamaño)
        - permite sistemas numéricos (octal, hexadecimal, binario)
    - float -> representan números con coma o parte decimal (punto flotante de doble precisión)
    - complex -> representan números con parte real e imaginaria
"""

entero = 42
flotante = 3.14159
complejo = 3 + 4j

print(f"Entero: {entero} (tipo: {type(entero).__name__})")
print(f"Flotante: {flotante} (tipo: {type(flotante).__name__})")
print(f"Complejo: {complejo} (tipo: {type(complejo).__name__})")

# ==================== OPERACIONES BÁSICAS ====================
a, b = 10, 3
print(f"\nOperaciones con {a} y {b}:")
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"División: {a / b}")
print(f"División entera: {a // b}")
print(f"Módulo: {a % b}")
print(f"Potencia: {a ** b}")

# ==================== FUNCIONES MATEMÁTICAS ====================
import math   # importación de funciones en el módulo math -> para usarlas y operar con ellas, es necesario incorporarlas con import

numero = -7.8
print(f"\nFunciones con {numero}:")
print(f"abs(): {abs(numero)}")  # Valor absoluto
print(f"round(): {round(3.14159, 2)}")  # Redondea y define la cantidad de decimales detrás del punto que serán tomados en cuenta como segundo argumento
print(f"math.ceil(): {math.ceil(numero)}")  # Redondea hacia arriba
print(f"math.floor(): {math.floor(numero)}")  # Redondea hacia abajo

# Funciones útiles
numeros = [1, 5, 3, 9, 2]
print(f"\nCon lista {numeros}:")
print(f"min(): {min(numeros)}")  # retorna el valor menor de la lista
print(f"max(): {max(numeros)}")  # retorna el valor mayor de la lista
print(f"sum(): {sum(numeros)}")  # retorna la suma entre todos los números de la lista

# ==================== CONVERSIONES ====================
print(f"\n--- CONVERSIONES ---")  # también aplican entre ellos (ej.: se puede convertir un int a float, etc.)
texto_numero = "123"
numero_texto = 456

print(f"int('{texto_numero}'): {int(texto_numero)}")
print(f"float('{texto_numero}'): {float(texto_numero)}")
print(f"str({numero_texto}): '{str(numero_texto)}'")

# ==================== EJERCICIO: calculadora de promedio ====================
print("\n--- CALCULADORA DE PROMEDIO ---")
calificaciones = [85.5, 90, 78.5, 92, 88]
promedio = sum(calificaciones) / len(calificaciones)
print(f"Calificaciones: {calificaciones}")
print(f"Promedio: {round(promedio, 1)}")
print(f"Nota más alta: {max(calificaciones)}")
print(f"Nota más baja: {min(calificaciones)}")


"""
Booleanos -> es un tipo de dato que solo puede tener dos valores: True o False
    - Son la respuesta retornada por los operadores lógicos y los operadores de comparación, con los cuales se hacen estructuras condicionales
    - Evalúan solo lo necesario

OPERADORES LÓGICOS:
    - and -> retorna True SOLO SI AMBAS condiciones son TRUE
    - or -> retorna False SOLO SI AMBAS condiciones son FALSE; de lo contrario, mientras que una condición sea True, retorna True
    - not -> retorna el valor invertido. Si es True, retorna False y viceversa

OPERADORES DE COMPARACIÓN:
    - < (menor que...) -> retorna true si el primero es menor que el segundo
    - <= (menor o igual que...) -> retorna true si el primero es menor o igual al segundo
    - > (mayor que...) -> retorna true si el primero es mayor que el segundo
    - >= (mayor o igual que...) -> retorna true si el primero es mayor o igual que el segundo
    - != (diferente que...) -> retorna true si el primero es diferente del segundo
    - == (igual que...) -> retorna True si el primero es exactamente igual al segundo (tanto en valor como en tipo de dato)

"""

# ==================== VALORES BOOLEANOS ====================
verdadero = True
falso = False
print(f"True: {verdadero} (tipo: {type(verdadero).__name__})")
print(f"False: {falso} (tipo: {type(falso).__name__})")

# ==================== OPERADORES LÓGICOS ====================
a, b = True, False
print(f"\nOperadores lógicos:")
print(f"True and False: {a and b}")
print(f"True or False: {a or b}")
print(f"not True: {not a}")
print(f"not False: {not b}")

# ==================== VALORES FALSY Y TRUTHY ====================
# son valores que se evalúan como False o True, pero que no son específicados con las palabras clave True o False
print(f"\n--- VALORES FALSY (se evalúan como False) ---")
falsy_valores = [0, 0.0, "", [], {}, None, False]
for valor in falsy_valores:
    print(f"bool({repr(valor)}): {bool(valor)}")

print(f"\n--- VALORES TRUTHY (se evalúan como True) ---")
truthy_valores = [1, -1, "hola", [1], {"a": 1}, True]
for valor in truthy_valores:
    print(f"bool({repr(valor)}): {bool(valor)}")

# ==================== COMPARACIONES ====================
x, y = 5, 10
print(f"\n--- COMPARACIONES con {x} y {y} ---")
print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} <= {y}: {x <= y}")