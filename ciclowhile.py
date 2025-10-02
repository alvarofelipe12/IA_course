# i = 1
# while i <= 10:
#     print(i*5)
#     i += 1

""""
Modificar el código para que le pregunte al usuario cual tabla quere y la muestre
"""

# tableNumber = int(input("Ingrese el nuúmero de la tabla que requiere:"))
# i = 1
# while i <= 10:
#     print(f"{tableNumber} x {i} = {i*tableNumber}")
#     i+=1

""""
Supongamos que tenemos una tienda. Le va a preguntar al usuario cuantos artículos va a comprar
luega vamos a emepzar a preguntarle el precio del artículo 1, 2, 3... hasta el último artículo.
luego le vamos a decir cuanto es el valor total de la compra.
"""

# articles = int(input("Bienvenido a la tienda 'No hay quien le atienda', cuántos artículos va a comprar: "))
# total = 0
# i = 1
# while i <= articles:
#     priceArticle = int(input(f"Por favor ingrese el precio para el artículo {i}: $"))
#     total += priceArticle
#     i += 1
# print(f"El valor total de su compra es de ${total}")

# option = 0
# redCounter = 0
# blueCounter = 0
# while option !=3:
#     print("Vamos a hacer la votación")
#     print("1. Candidato rojo")
#     print("2. Candidato azul")
#     print("3. Terminar")
#     option = int(input("ingrese una opción: "))
#     if option == 1:
#         redCounter += 1
#     elif option == 2:
#         blueCounter += 1
# print(f"El candidato rojo obtuvo {redCounter} votos")
# print(f"El candidato azul obtuvo {blueCounter} votos")

""""
Nidufucak ek código para que en caso de que el usuario elija una opción dieferente a 1 || 2 || 3
muestre un mensaje diciendo que la opción es inválida
"""
# option = 0
# redCounter = 0
# blueCounter = 0
# while option !=3:
#     print("Vamos a hacer la votación")
#     print("1. Candidato rojo")
#     print("2. Candidato azul")
#     print("3. Terminar")
#     option = int(input("ingrese una opción: "))
#     if option == 1:
#         redCounter += 1
#     elif option == 2:
#         blueCounter += 1
#     elif option != 3:
#         print("Opción inválida")
# print(f"El candidato rojo obtuvo {redCounter} votos")
# print(f"El candidato azul obtuvo {blueCounter} votos")

""""
Restaurante las delicias
1. Bandeja paisa $20k
2. Ajiaco $12k
3. Fiambre $16k
4. Terminar pedido

Cuando el usuario indique la opción 4 debemos mostrar el total de la factura
"""

# option = 0
# first_opt_counter = 0
# second_opt_counter = 0
# third_opt_counter = 0
# while option != 4:
#     print("1. Bandeja paisa $20.000")
#     print("2. Ajiaco $12.000")
#     print("3. Fiambre $16.000")
#     print("4. Terminar pedido")
#     option = int(input("Elija un plato del menú: "))
#     if option == 1:
#         first_opt_counter += 1
#     elif option == 2:
#         second_opt_counter += 1
#     elif option == 3:
#         third_opt_counter += 1
#     elif option !=4:
#         print("Opción invalida, intente de nuevo\n------------")
# total_first_opt = first_opt_counter * 20000 
# total_second_opt = second_opt_counter * 12000 
# total_third_opt = third_opt_counter * 16000 
# total = total_first_opt + total_second_opt + total_third_opt
# if first_opt_counter > 0:
#     print(f"{first_opt_counter} x Bandeja paisa...... ${total_first_opt}")
# if second_opt_counter > 0:
#     print(f"{second_opt_counter} x Ajiaco............. ${total_second_opt}")
# if third_opt_counter > 0:
#     print(f"{third_opt_counter} x Fiambre............ ${total_third_opt}")
# print(f"Total: ${total}")

""""
=== SISTEMA DE LOGIN ===
Ejercicio: Sistema de Login con Intentos Limitados
Descripción del Problema:
Desarrolla un programa que simule un sistema de login seguro con las siguientes características:

Usuario y contraseña predefinidos:

Usuario: "admin"

Contraseña: "1234"

Funcionalidades requeridas:

Máximo 3 intentos de login

Mensajes diferentes según el error

Opción para recuperar contraseña después de 2 intentos fallidos

Menú principal después del login exitoso

=== MENÚ PRINCIPAL ===
1. Ver perfil
2. Cambiar contraseña
3. Salir
Selecciona una opción:

Pistas para los estudiantes:
Estructura general:

Usar while para controlar los intentos

Usar if/elif/else para verificar credenciales

Contador de intentos

Validaciones importantes:

Verificar primero si se excedieron los intentos

Comparar usuario y contraseña por separado

Manejar la opción de recuperación

Extras opcionales (para estudiantes avanzados):

Agregar más usuarios al sistema

Guardar historial de intentos fallidos

Bloquear usuario después de muchos intentos
"""

user = "admin"
password = "1234"
tries_counter = 3
menu = """
1. Ver perfil
2. Cambiar contraseña
3. Salir
Selecciona una opción:"""
option = 0

while tries_counter > 0:
    userInput = input("Ingrese su usuario: ")
    passwordInput = input("Ingrese su contraseña: ")
    if user == userInput and passwordInput == password:
        option = int(input(menu))
    else:
        print("Usuario o contraseña equivocada")
        if tries_counter == 1:
            pass_recovery = input("Desea recuperar la contraseña? responda si o no: ")
            if pass_recovery == "si":
                print("Su contraseña es: 1234")
        tries_counter -= 1
        

