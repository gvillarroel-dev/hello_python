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


# ================================= Ejercicio: crear un programa que pida nombre, edad y altura, y muestre un mensaje personalizado ================================= 
name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")
height = input("Ingrese su altura: ")

print(f"Hola, {name}. Tienes {age} años y tienes una estatura de {height}mts")


# ================================= EJERCICIO: el usuario debe ingresar una frase y luego debe poder modificar una palabra específica ================================= 
sentence = input("Ingrese su frase: ")
print(f"Su frase es: {sentence}")
word_1 = input("Ingrese la palabra a reemplazar: ")
word_2 = input("Ingrese la palabra que reemplazará la palabra anterior: ")
print(sentence.replace(word_1, word_2))