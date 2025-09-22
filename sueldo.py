""""
nombre = input("Ingrese su nombre: ")
print("Hola", nombre, "bienvenido a la programación en python")
"""

""""
Hacer un programa que le pida al usuario el valor de la hora trabajada y la cantidad de horas trabajadas en el mes.
Al final debe mostrar el sueldo mensual del trabajador.
"""


""""
priceHour = int(input("Ingrese el valor de la hora trabajada: "))
qtyHours = int(input("Ingrese el número de horas trabajadas: "))
monthlySalary = priceHour * qtyHours
print("El sueldo mensual es de $", monthlySalary)
"""

""""
Preguntar al usuario dos numeros y mostrar el resultado de:
suma, resta, multiplicación, división, potencia, módulo y división entera
"""

firstNumber = float(input("Ingrese el primer número: "))
secondNumber = float(input("Ingrese el segundo número: "))
addition = firstNumber + secondNumber
substraction = firstNumber - secondNumber
multiplication = firstNumber * secondNumber
division = firstNumber / secondNumber
exp = firstNumber ** secondNumber
modulus = firstNumber % secondNumber
floorDivision = firstNumber // secondNumber

print("El resultado de la suma es: ", addition)
print("El resultado de la resta es: ", substraction)
print("El resultado de la multiplicación es: ", multiplication)
print("El resultado de la división es: ", division)
print("El resultado de la potenciación es: ", exp)
print("El resultado del módulo es: ", modulus)
print("El resultado de la división entera es: ", floorDivision)