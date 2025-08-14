"""
FUNCIÓN -> bloque de instrucciones con un nombre definido que hace una tarea específica
    - Puede ser invocado en cualquier lugar del código después de su definición
    - Siempre debe retornar algo

    RETURN -> declaración usada para obtener una respuesta de la ejecución de una función (o de la operación/tarea que la función realiza)
"""

def saludo_simple():
    nombre = input("Ingrese su nombre: ")
    return f"Hola, {nombre}. ¡Bienvenidx!"
saludo = saludo_simple()
print(saludo)

# función con parámetros -> permite recibir datos con los que operará internamente para obtener un resultado
def saludo_con_argumento(nombre):
    return f"¡Bienvenido, {nombre}!"

saludo = saludo_con_argumento("Hikaru")
print(saludo)

# función con múltiples parámetros -> los argumentos se leen en orden, por lo que deben corresponder con el parámetro que quieren ocupar
def saludo_con_edad(nombre, edad):
    return f"¡Bienvenido, {nombre}! Tienes {edad} años."

saludo = saludo_con_edad("Yuuno", 22)
print(saludo)


# función con parámetros indefinidos -> *param indica que se estarán pasando varios argumentos como una tupla (lista de valores), pero no se sabe la cantidad exacta
def saludo_funcion(*nombres):
    return f"Hola, {nombres}. ¡Bienvenido(s)!"

saludo = saludo_funcion("Yuuno", "Hikaru", "Kafka")
print(saludo)

# función que suma dos números y recibe esos valores mediante inputs
def suma(num_1, num_2):
    return num_1 + num_2

num_1 = int(input("Ingrese el primer número a sumar: "))
num_2 = int(input("Ingrese el segundo número a sumar: "))
print(suma(num_1, num_2))


# ================================================================================
#                                EJERCICIOS DE FUNCIONES
# ================================================================================
"""
Crea una función llamada 'calcular_area_rectangulo' que tome ancho y alto
como parámetros y retorne el área del rectángulo.
Incluye validación para que los valores sean positivos.
"""
def calcular_area_rectangulo(ancho, alto):
    if ancho < 0 or alto < 0:
        return "ERROR: Las dimensiones deben ser positivas."
    else:
        return f"El área del rectángulo es: {ancho * alto}"

print("\n=========== Ejercicio 1: área del rectángulo ===========\n")
print(calcular_area_rectangulo(6, 4))
print(calcular_area_rectangulo(2, -4))
print(calcular_area_rectangulo(-2, 4))
print(calcular_area_rectangulo(3, 10))


"""
Crea una función llamada 'crear_perfil_usuario' que tome:
- nombre (obligatorio)
- edad (obligatorio)
- ciudad (opcional, por defecto "No especificada")
- profesion (opcional, por defecto "No especificada")

La función debe retornar un diccionario con toda la información.
"""

def crear_perfil_usuario(nombre, edad, ciudad=False, profesion=False):
    perfil_usuario = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": "No disponible" if not ciudad else ciudad,
        "profesion": "No disponible" if not profesion else profesion
    }
    return perfil_usuario

print("\n=========== Ejercicio 2: perfil de usuarios ===========\n")
print(crear_perfil_usuario("Hikaru", 26, "Tokio", "Actor"))
print(crear_perfil_usuario("Ailee", 18))
print(crear_perfil_usuario("Hinata", 32, "Kioto"))

"""
Crea una función llamada 'estadisticas_lista' que tome una lista de números
y retorne un diccionario con:
- suma total
- promedio
- número mayor
- número menor
- cantidad de elementos

Si la lista está vacía, debe manejar el error apropiadamente.
"""
def estadisticas_lista(iterable):
    if not iterable:
        return "--ERROR: El elemento no puede estar vacío para operar."
    else:
        lista = {
            "suma_total": sum(iterable),
            "promedio": sum(iterable) / len(iterable),
            "numero_mayor": max(iterable),
            "numero_menor": min(iterable),
            "cantidad_elementos": len(iterable)
        }
        return lista

print("\n=========== Ejercicio 3: lista de estadisticas ===========\n")
print(estadisticas_lista([0, 2, 4, 6, 8]))
print(estadisticas_lista([12]))
print(estadisticas_lista([]))


"""
- Función recursiva y decorador
    Parte A: Crea una función recursiva llamada 'factorial' que calcule el factorial de un número.
    Parte B: Crea un decorador simple llamado 'medir_tiempo' que mida el tiempo de ejecución.
    Parte C: Aplica el decorador a la función factorial.


DECORADOR -> es una función que toma otra función como argumento y retorna una versión modificada de ella
    - Puede modificar o extender el comportamiento de funciones sin cambiar su código original
    - Usos comunes -> aplicar la misma funcionalidad a múltiples funciones de forma reutilizable y limpia
        - Medir tiempo de ejecución
        - Logging (registro de eventos)
        - Validación de permisos
        - Cache de resultados
        - Manejo de errores
    
    - Sintaxis básica:
        @decorador
        def mi_funcion():
        pass

--------- Ejemplo rápido ---------
def mi_decorador(func):
    def wrapper():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()

"""
import time
from functools import wraps

# decorador para medir_tiempo
def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        return resultado, tiempo_ejecucion
    return wrapper

# función recursiva con decorador
@medir_tiempo
def factorial(num):
    if num < 0:
        return "ERROR: El factorial no está definido para números negativos."
    if num == 0 or num == 1:
        return 1
    
    # recursividad
    return num * factorial(num - 1)[0] # toma solo el valor, no el tiempo

print("\n=========== Ejercicio 4: factorial con recursividad ===========\n")

resultado, tiempo = factorial(3)
print(f"Factorial recursivo de 3: {resultado} \tTiempo de respuesta: {tiempo:.4f}")

resultado, tiempo = factorial(7)
print(f"Factorial recursivo de 7: {resultado} \tTiempo de respuesta: {tiempo:.4f}")

resultado, tiempo = factorial(123)
print(f"Factorial recursivo de 2: {resultado} \tTiempo de respuesta: {tiempo:.4f}")