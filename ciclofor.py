""""
a = 1
while a <= 10:
    print(f"while {a}")
    a += 1

for i in range(1,11):
    print(f"for {i}")
"""

# for i in range(2,21,2):
#     print(i)

""""
pedir al usuario cual tabla quiere y la vamos a mostrar pero usando ciclo for
"""

# table_number = int(input("Que tabla quiere?: "))
# # for i in range(1, 11):
# #     print(i*table_number)
# for i in range(1*table_number, 10*table_number+1, table_number):
#     print(i)

""""
Hacer las diez tablas de multiplicar utilizando ciclo for
"""
# for i in range(1,11):
#     print(f"Tabla del {i}\n")
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print("---------------------\n")

# cadena = "murciélago"
# for i in cadena:
#     print(i)

# fruta  = "manzana"
# for x in fruta:
#     print(x)
#     if x == "z":
#         break

# fruta  = "manzana"
# for x in fruta:
#     if x == "z":
#         continue
#     print(x)

""""
Ejercicio: Cajero Automático

Escribe un programa en Python que simule un cajero automático simple:

El programa debe mostrar un menú con las siguientes opciones:

Consultar saldo

Retirar dinero

Depositar dinero

Salir

El saldo inicial es de $1000.

El usuario puede retirar dinero siempre que tenga saldo suficiente.

El depósito suma dinero al saldo.

El programa debe repetirse (ciclo while) hasta que el usuario elija la opción Salir (4).
"""

menu = """
1. Consultar saldo
2. Retirar dinero
3. Depositar dinero
4. Salir
"""
balance = 1000
option = 1
while option < 4 and option > 0:
    print("-- Bienvenido--")
    print(menu)
    option = int(input("Ingrese una opción: "))
    if option == 1:
        print(f"Su saldo actual es: ${balance}")
    elif option == 2:
        money_to_withdraw = int(input("Cuánto dinero desea retirar?: "))
        if money_to_withdraw > balance:
            print("Saldo insuficiente")
        else:
            balance -= money_to_withdraw
            print(f"Retiro exitoso. Su nuevo saldo es: ${balance}")
    elif option == 3:
        deposit_amount = int(input("Cuánto desea depositar?: "))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"Depósito exitoso. Su nuevo saldo es: ${balance}")
        else:
            print("Error. Por favor ingrese una cantidad mayor a cero")
print("Gracias por usar este cajero. Feliz día!")