# edad = int(input("Ingrese su edad: "))
# print("Hola tu edad es", edad, "años")
# if edad >= 18:
#     print("eres mayor de edad y puedes votar")
#     print("puedes comprar cerveza")
# else:
#     print("eres menor de edad y no puedes votar")
# print("esta instrucción siempre se ejecuta")

"""
Crear un programa que pregunte al usuario el salario y:
Si gana menos de dos millones, incrementar el salario en 200000 y mostrar el valor a devengar,
de lo contrario, mostrar un mensaje qu diga que no tiene derecho a subsidio
"""

# salary = int(input("Ingresa tu salario actual: "))
# if salary < 2000000:
#     salary += 200000
# else:
#     print("No tienes derecho a subsidio 😞")
# #  modificar el codigo para que muestre siempre la cantidad a recibir
# print("Su salario es de", salary)

""""
Modificar el código para que saque un mensaje de edad inválida
si la edad ingresada es un número negativo o mayor a 120
"""
# edad = int(input("Ingrese la edad: "))
# if edad >= 0 and edad < 6:
#     print("primera infancia")
# elif edad >= 6 and edad < 12:
#     print("Niñez")
# elif edad >= 12 and edad < 18:
#     print("Adolescencia")
# elif edad >= 18 and edad <= 120:
#     print("Adulto")
# else:
#     print("Edad invalida")

""""
Pedir un numero al usuario entre 1 y 7
1 lunes
2 martes
3 miercoles
4 jueves
5 viernes
6 sábado
7 domingo
cualquier otro número decir que es invalido
"""
number = int(input("Ingrese un número"))
if number == 1:
    print("Lunes")
elif number == 2:
    print("Martes")
elif number == 3:
    print("Miercoles")
elif number == 4:
    print("Jueves")
elif number == 5:
    print("Viernes")
elif number == 6:
    print("Sábado")
elif number == 7:
    print("Domingo")
else:
    print("Ese día es invalido")