# ========================================================================
#                       EJERCICIOS CON ESTRUCTURAS DE CONTROL
# ========================================================================

"""
EJERCICIO 1: clasificador de números 
    - El programa solicitará números al usuario continuamente hasya que el usuario ingrese 0 (cero)
    - Para cada número ingresado, el programa deberá:
        * determinar si es positivo, negativo o cero
        * indicar si es par o impar -> solo si no es cero
        * contar cuántos números de cada tipo ingresaron
        * al finalizar, mostrar las estadísticas completas
    
    - Ejemplo de salidas:
        # ingresa un número (0 para salir): 15
        # 15 es positivo e impar
        # Ingresa un número (0 para salir): -8
        # -8 es negativo y par

        ======= ESTADÍSTICAS =======
        Números positivos: 1
        Números negativos: 1
        Números pares: 1
        Números impares: 1


"""

def clasificador():
    positivos = negativos = pares = impares = 0

    while True:
        try:
            numero = int(input("Ingresa un número (0 para salir): "))

            # clasificación de números positivos, negativos o neutros
            if numero > 0:
                print(f"{numero} es positivo", end="")
                positivos += 1
            elif numero < 0:
                print(f"{numero} es negativo", end="")
                negativos += 1
            else:
                print("\nGracias por visitar el clasificador de números. \n¡Nos vemos luego!")
                break

            # clasificación de números pares, impares (solo si no es cero)
            if numero % 2 == 0:
                print(" y par")
                pares += 1
            else:
                print(" e impar")
                impares += 1

            # manejo de errores
        except ValueError:
            print("ERROR: Ingresa solo números enteros.")
            continue
        
        # mostrar estadísticas
        print("======= ESTADÍSTICAS =======")
        print(f"Números positivos: {positivos}")
        print(f"Números negativos: {negativos}")
        print(f"Números pares: {pares}")
        print(f"Números impares: {impares}")
        print(f"Total de números ingresados: {positivos + negativos}")
    
# clasificador()


"""
EJERCICIO 2: Generador de patrones
    - El programa generará diferentes patrones geométricos usando asteriscos (*)
    - El usuario debe poder elegir entre 4 tipos de patrones y especificar el tamaño -> el tamaño indicará la cantidad de * verticales y horizontales base
    - Opciones:
        1. Triángulo rectángulo
        2. Pirámide centrada
        3. Rombo
        4. Cuadrado hueco

"""
def triangulo_rectangulo(tamano):
    print("\n-------- Triángulo Rectángulo --------")
    for i in range(1, tamano + 1):
        print("*" * i)

def piramide_centrada(tamano):
    print("\n-------- Pirámide Centrada --------")
    for i in range(1, tamano + 1):
        espacios = " " * (tamano - i)
        items = "*" * (2 * i - 1)
        print(espacios + items)

def rombo(tamano):
    print("\n-------- Triángulo Rectángulo --------")
    
    # parte superior
    for i in range(1, tamano + 1):
        espacios = " " * (tamano - i)
        items = "*" * (2 * i - 1)
        print(espacios + items)

    # parte inferior
    for i in range(tamano - 1, 0, -1):
        espacios = " " * (tamano - i)
        items = "*" * (2 * i - 1)
        print(espacios + items)


def cuadrado_hueco(tamano):
    print("\n-------- Cuadrado hueco --------")
    
    for i in range(tamano):
        if i == 0 or i == (tamano - 1):
            # define la primera y última línea con todos los *
            print("*" * tamano)
        else:
            print("*" + (" " * (tamano - 2)) + "*")

# función principal -> menú de opciones + llamada a funciones específicas

def main():
    while True:
        print("\n--- Menú de Patrones ---")
        print("1. Triángulo rectángulo")
        print("2. Pirámide centrada")
        print("3. Rombo")
        print("4. Cuadrado hueco")
        print("5. Mostrar todos los patrones")
        print("6. Salir")
    
        # opciones y llamadas a función
        try:
            opcion = int(input("\nSeleccione una opción (1-6): "))

            if opcion == 6:
                print("¡Gracias por usar el generador de patrones!")
                break
            
            if opcion in [1, 2, 3, 4, 5]:
                tamano = int(input("Ingrese el tamaño del patron (3-20): "))

                if tamano < 3 or tamano > 20:
                    print("El tamaño debe estar entre 3 y 20.")
                    continue

                if opcion == 1:
                    triangulo_rectangulo(tamano)
                elif opcion == 2:
                    piramide_centrada(tamano)
                elif opcion == 3:
                    rombo(tamano)
                elif opcion == 4:
                    cuadrado_hueco(tamano)
                elif opcion == 5:
                    triangulo_rectangulo(tamano)
                    piramide_centrada(tamano)
                    rombo(tamano)
                    cuadrado_hueco(tamano)
                else:
                    print("Opción no válida. Selecciona del 1 al 6.")

        except ValueError:
            print("ERROR: Ingrese solo números enteros.")
        
        input("\nPresiona 'Enter' para continuar...")

main()