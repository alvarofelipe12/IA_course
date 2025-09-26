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

articles = int(input("Bienvenido a la tienda 'No hay quien le atienda', cuántos artículos va a comprar: "))
total = 0
i = 1
while i <= articles:
    priceArticle = int(input(f"Por favor ingrese el precio para el artículo {i}: $"))
    total += priceArticle
    i += 1
print(f"El valor total de su compra es de ${total}")