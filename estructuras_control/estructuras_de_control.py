"""
Estructuras de control -> bloques que permiten controlar el flujo de ejecución de un programa
    - Permiten determinar qué instrucciones se ejecutan, en qué orden y bajo qué condiciones
    - Son esenciales para crear estructuras que tomen decisiones y repitan tareas

3 tipos:
    - Estructuras condicionales -> ejecutan código según se cumplan o no ciertas condiciones
    - Estructuras repetitivas -> ejecutan código de forma repetida mientras se cumpla una condición
    - Estructuras de control de flujo -> alteran el flujo normal de ejecución dentro de bucles o funciones

"""

# =======================================================================
#                            IF-ELSE: sintax
# =======================================================================

"""
if -> ejecuta un determinado bloque de código dependiendo de si la condición evaluada es verdadera

else -> ejecuta un bloque de código si la condición impuesta por if es False
    - En caso de que hayan varios casos para evaluar, else se ejecutará si, tras evaluar cada condición, ninguna resulta ser True

elif -> permite agregar otros casos de condición (o evaluaciones condicionales) para evaluar una condición específica diferente a la impuesta en if
"""


edad = 17
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# ejemplo con if-elif-else
nota = 75
if nota >= 90:
    print("¡Excelente!")
elif nota >= 70:
    print("Bueno")
else:
    print("Necesitas mejorar...")


# =======================================================================
#                            BUCLES: for, while
# =======================================================================
"""
Bucle for -> usado para iterar sobre secuencias (listas, tuplas, strings, rangos, etc.) un NÚMERO CONOCIDO de veces
    - Usado cuando se saben los ciclos de iteración necesitados
    - sintax:
        for variable in secuencia:
            # código a ejecutar

Bucles while -> se ejecuta mientras una condición sea verdadera
    - Usado cuando no se sabe exactamente cuántas veces se repetirá
    - sintax:
        while condición:
            # código a ejecutar
            # actuarlizar variable de control (para llegar al fin del bucle en algún momento) -> sin ella, se produce un bucle infinito
"""

# ============================= EJEMPLOS: uso de For =============================

frutas = ["arándano", "pomelo", "kiwi", "limón"]
for fruta in frutas:
    print(f"Me gusta el {fruta}")

# ejemplo de for usando range() -> range es una función integrada que genera una secuencia (lista) de números en un rango indicado (según ciertas configuraciones, basados en argumentos pasados, su comportamiento puede cambiarse)
print("------------- for con range() pasando solo un argumento -------------")
for num in range(5):
    print(f"Número: {num}")

print("\n------------- range() pasando dos argumentos -------------")
for i in range(2, 9):  # indica desde qué número generar la secuencia numérica y el final de la misma (no incluido)
    print(f"Número: {i}")

print("\n------------- range() pasando tres argumentos -------------")
for x in range(0, 11, 2):  # indica inicio de la secuencia, final de la secuencia (no incluido) y el salto entre números dentro de la secuencia
    print(f"Número: {x}")

# EJEMPLO: iterando sobre strings
palabra = "Python"
for letra in palabra:
    print(letra)


# ============================= EJEMPLOS: uso de While =============================
print("\n------------- ejemplos con while -------------")
print("\n----- CONTADOR -----")
# contador básico
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# bucle con entrada de usuario
print("\n----- Entrada de usuario -----")
respuesta = ""
while respuesta.lower() != "salir":
    respuesta = input("Escribe 'salir' para terminar de escribir: ")
    print(f"Ingresaste: {respuesta}")


# bucle con validación de entrada
print("\n----- Validación de entrada -----")
numero = -1
while numero < 0 or numero > 100:
    numero = int(input("Ingrese un número entre 0 y 100: "))
print(f"Número válido: {numero}")



# =======================================================================
#                            CONTROL DE FLUJO: continue, break
# =======================================================================
"""
Break -> sentencia que termina el bucle inmediatamente
Continue -> salta a la siguiente iteración

else -> también puede ser usado con bucles, no solo con condicionales
    - se ejecuta si el bucle termina normalmente (sin break)
"""

# ejemplo de for con break
for i in range(10):
    if i == 5:
        break
    print(i)


# ejemeplo de for con continue
for i in range(5):
    if i == 2:
        continue
    print(i)

# ejemplo de for con else
for i in range(3):
    print(i)
else:
    print("¡Bucle completado!")