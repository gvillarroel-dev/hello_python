# =================================== EJERCICIOS CON INT ===================================

"""
Ejercicio 1: calculadora de tiempo
    - Debe convertir segundos a formato legible -> RESULTADO ESPERADO >> entrada: 7265; salida: "2 horas, 1 minuto, 5 segundos"
    - Debe calcular las horas -> segundos / 3600 (segundos en 1 minuto)
    - Debe calcular los minutos restantes antes del cambio de hora -> (segundos % 3600) / 60 >>> el resto de la conversión de minutos en segundos, dividido 60 (límite de 1 minuto)
    - Debe calcular los segundos finales usando módulo -> minutos % 60
"""
# print("¡Bienvenido a la calculadora de tiempo!")
# segundos_entrada = int(input("Ingrese los segundos a calcular: "))

# hora = f"{segundos_entrada // 3600} hora(s)"
# minutos = f"{(segundos_entrada % 3600) // 60} minuto(s)"
# segundos = f"{segundos_entrada % 60} segundo(s)"

# print(f"Entrada de datos: {segundos_entrada}")
# print(f"Resultado: {hora}, {minutos}, {segundos}")


"""
Ejercicio 2: Sistema de análisis de ventas diarias
    - Procesará ventas de una semana, calculará el total de ventas
    - Encontrará el día con más y menos ventas
    - Calculará la diferencia entre el mejor y peor día de venta
"""
# ventas = [90, 20, 30, 50, 100, 230, 190]
# dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# total_ventas = sum(ventas)
# mejor_dia_indice = ventas.index(max(ventas))
# peor_dia_indice = ventas.index(min(ventas))
# diferencia = max(ventas) - min(ventas)

# print(f"Ventas por día: {dict(zip(dias, ventas))}")
# print(f"Ventas totales de la semana: ${total_ventas}")
# print(f"- Mejor día de venta: {dias[mejor_dia_indice]} - ${ventas[mejor_dia_indice]}")
# print(f"- Peor día de venta: {dias[peor_dia_indice]} - ${ventas[peor_dia_indice]}")
# print(f"Diferencia mejor-peor: ${diferencia}")



# =================================== EJERCICIOS CON FLOAT ===================================

"""
Ejercicio 3: Calculadora de interés compuesto
    - Calculará el crecimiento de inversión -> ganancia total
    - Datos:
        - Capital inicial = 5000.00
        - Tasa anual = 7.5%
        - Periodo = 5 años
        - Fórmula >>> monto = capital * ((1 + tasa) ** años)

"""
# capital_inicial = 5000.00
# tasa_anual = 0.075
# periodo_ano = 5

# print(f"Capital inicial: ${capital_inicial}")
# print(f"Tasa Anual: {tasa_anual * 100}%")
# print(f"Periodo de tiempo: {periodo_ano} años\n")

# monto_actual = capital_inicial
# for ano in range(1, periodo_ano + 1):
#     monto_anterior = monto_actual
#     monto_actual = capital_inicial * ((1 + tasa_anual) ** ano)
#     ganancia_anual = monto_actual - monto_anterior
#     print(f"{ano}\t${monto_actual:.2f}\t${ganancia_anual:.2f}")

# ganancia_total = monto_actual - capital_inicial
# print(f"\nGanancia total: ${ganancia_total:.3f}")


# =================================== EJERCICIOS CON STRING ===================================

"""
Ejercicio 4: Programa que reemplaza texto de una cadena o frase
    - El usuario ingresará una frase o texto
    - El usuario podrá elegir qué palabra cambiar del texto
    - El usuario ingresará la palabra que reemplazará la palabra señalada
"""

# frase = input("Ingrese una frase: ")
# reemplazar = input("Ingrese la palabra a reemplazar: ")
# reemplazo = input("Ingrese la palabra de reemplazo: ")

# print(f"\nFrase original: {frase}")
# print(f"Frase a reemplazar: {reemplazar}")
# print(f"Frase de reemplazo: {reemplazo}")
# print(f"--- Frase actualizada: '{frase.replace(reemplazar, reemplazo)}' ---")


# =================================== EJERCICIOS CON VALORES LÓGICOS ===================================

"""
Ejercicio 5: Sistema de acceso
    - El sistema evaluará los permisos de usuario
    - Reglas:
        - acceso total -> administrador = True
        - acceso normal -> (empleado and credencial) and dia_laboral
        - acceso denegado -> not(condiciones anteriores)
    - El sistema verificará si el usuario:
        - Es empleado
        - Tiene credencial
        - Es día laboral
        - Es administrador
"""

# casos_prueba = [
#     { "es_admin": True, "es_empleado": True, "tiene_credencial": True, "dia_laboral": True},
#     { "es_admin": False, "es_empleado": True, "tiene_credencial": True, "dia_laboral": True},
#     { "es_admin": False, "es_empleado": True, "tiene_credencial": False, "dia_laboral": True},
#     { "es_admin": False, "es_empleado": True, "tiene_credencial": True, "dia_laboral": False},
#     { "es_admin": False, "es_empleado": False, "tiene_credencial": True, "dia_laboral": True},
# ]

# for i, caso in enumerate(casos_prueba, 1):
#     es_admin = caso["es_admin"]
#     es_empleado = caso["es_empleado"]
#     tiene_credencial = caso["tiene_credencial"]
#     dia_laboral = caso["dia_laboral"]

#     # validaciones de acceso
#     acceso_total = es_admin
#     acceso_normal = (es_empleado and tiene_credencial) and dia_laboral
#     acceso_denegado = not(acceso_normal or acceso_total)

#     # lógica y verificación de acceso
#     if acceso_total:
#         resultado = "Acceso Total - Administrador"
#     elif acceso_normal:
#         resultado = "Acceso Normal - Empleado"
#     else:
#         resultado = "Acceso Denegado"

#     print(f"Caso: {i} - Admin: {es_admin}\tEmpleado: {es_empleado}\tTiene credencial: {tiene_credencial}\tDía laboral: {dia_laboral}")
#     print(f"--- Resultado de acceso: {resultado} ---\n")



"""
Ejercicio 6: Validador de formulario
    - El sistema validará datos de registro:
        - Edad >= 18
        - email correcto (formato)
        - contraseña >= 8
        - terminos aceptados = True
    - El sistema mostrará mensajes específicos para cada error
"""

# # datos de entrada
# datos_form = {
#     "edad": 26,
#     "email": "FHijaku@email.com",
#     "contraseña": "NH3mj#ke1&@h",
#     "terminos_aceptados": True
# }

# # validaciones individuales 
# edad_valida = datos_form["edad"] >= 18
# email_valido = "@" in datos_form["email"] and ".com" in datos_form["email"]
# contrasena_valida = len(datos_form["contraseña"]) >= 8
# terminos_ok = datos_form["terminos_aceptados"]

# # validación de formulario completo
# form_valido = edad_valida and email_valido and contrasena_valida and terminos_ok

# # impresiones en pantalla
# print(f"Datos ingresados: {datos_form}")
# print(f"\n--- Validaciones individuales ---")
# print(f"- Edad >= 18: {"✓" if edad_valida else "✗"} ({"Válida" if edad_valida else "Inválida"})")
# print(f"- Email: {"✓" if email_valido else "✗"} ({"Válida" if email_valido else "Inválida"})")
# print(f"- Contraseña > 8 caracteres: {"✓" if contrasena_valida else "✗"} ({"Válida" if contrasena_valida else "Inválida"})")
# print(f"- Terminos Aceptados: {"✓" if terminos_ok else "✗"} ({"Aceptados" if terminos_ok else "Negados"})")
# print(f"\n----- Validación del formulario -----")
# print(f"RESULTADO FINAL: {"Formulario Válido" if form_valido else "Formulario Inválido"}")

# =================================== EJERCICIOS INTEGRADORES ===================================

"""
1. Sistema de inventario
- Combina todos los tipos:
    - int -> codigos, cantidades, stock
    - float -> precios, descuentos, totales
    - string -> nombres, descripciones, categorías
    - booleanos -> disponible, en_oferta, activo

"""




"""
2. Procesador de calificaciones 
    - int -> num_de_estudiantes, intentos
    - float -> notas, promedios
    - string -> nombres, comentarios
    - booleanos -> aprobado, honor_roll
"""





"""
3. Juego de adivinanza: "Adivina el número secreto"
    - int -> número aleatorio secreto, intentos, puntaje
    - string -> pistas, mensajes, nombre del jugador
    - booleano -> adivinado, juego_activo
"""