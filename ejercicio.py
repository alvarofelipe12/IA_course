# EJERCICIO PRÁCTICO: CALCULADORA DE EVALUACIÓN DE META DE AHORROS

# === DATOS INICIALES ===
meta_ahorro = 10000
ahorro_actual = 7500
ingreso_mensual = 2000
gasto_mensual = 1500
meses_transcurridos = 6
total_meses = 12

# === OPERADORES ARITMÉTICOS ===
# Cálculos básicos
ahorro_mensual = ingreso_mensual - gasto_mensual  # Resta
ahorro_total_proyectado = ahorro_actual + (ahorro_mensual * (total_meses - meses_transcurridos))  # Suma y multiplicación
porcentaje_completado = (ahorro_actual / meta_ahorro) * 100  # División y multiplicación
diferencia_meta = meta_ahorro - ahorro_total_proyectado  # Resta
promedio_ahorro_mensual = ahorro_actual // meses_transcurridos  # División entera
resto_division = ahorro_actual % 1000  # Módulo
potencia_crecimiento = ahorro_mensual ** 2  # Potencia

# === OPERADORES DE ASIGNACIÓN ===
# Actualizaciones de valores
ahorro_actual += 500  # ahorro_actual = ahorro_actual + 500
gasto_mensual -= 200  # gasto_mensual = gasto_mensual - 200
ingreso_mensual *= 1.1  # ingreso_mensual = ingreso_mensual * 1.1
meta_ahorro /= 2  # meta_ahorro = meta_ahorro / 2
ahorro_mensual //= 2  # ahorro_mensual = ahorro_mensual // 2
resto_division %= 100  # resto_division = resto_division % 100
potencia_crecimiento **= 0.5  # potencia_crecimiento = potencia_crecimiento ** 0.5

# === OPERADORES DE COMPARACIÓN ===
# Evaluaciones booleanas
meta_alcanzable = ahorro_total_proyectado >= meta_ahorro
ahorro_suficiente = ahorro_actual > 5000
gastos_controlados = gasto_mensual < ingreso_mensual
mitad_camino = meses_transcurridos == total_meses / 2
meta_exacta = ahorro_actual == meta_ahorro
diferente_meta = ahorro_actual != meta_ahorro
menos_de_mitad = meses_transcurridos <= total_meses / 2

# === OPERADORES LÓGICOS ===
# Combinaciones lógicas
situacion_ideal = meta_alcanzable and gastos_controlados
situacion_riesgo = not gastos_controlados or ahorro_actual < 3000
situacion_estable = ahorro_suficiente and (gastos_controlados or ingreso_mensual > 2500)
es_viable = meta_alcanzable or (ahorro_mensual > 1000 and meses_transcurridos < 10)
combinacion_compleja = (ahorro_actual > 6000 and gasto_mensual < 1200) or (ingreso_mensual > 3000 and not menos_de_mitad)

# === MOSTRAR RESULTADOS ===
print("=== RESULTADOS DE LA EVALUACIÓN ===\n")

print("Datos iniciales:")
print(f"Meta de ahorro: ${meta_ahorro}")
print(f"Ahorro actual: ${ahorro_actual}")
print(f"Ingreso mensual: ${ingreso_mensual}")
print(f"Gasto mensual: ${gasto_mensual}")
print(f"Meses transcurridos: {meses_transcurridos}/{total_meses}\n")

print("Cálculos aritméticos:")
print(f"Ahorro mensual: ${ahorro_mensual}")
print(f"Ahorro total proyectado: ${ahorro_total_proyectado}")
print(f"Porcentaje completado: {porcentaje_completado}%")
print(f"Diferencia con meta: ${diferencia_meta}")
print(f"Promedio ahorro mensual: ${promedio_ahorro_mensual}")
print(f"Resto de división: {resto_division}")
print(f"Potencia de crecimiento: {potencia_crecimiento}\n")

print("Evaluaciones de comparación:")
print(f"¿Meta alcanzable? {meta_alcanzable}")
print(f"¿Ahorro suficiente? {ahorro_suficiente}")
print(f"¿Gastos controlados? {gastos_controlados}")
print(f"¿Mitad del camino? {mitad_camino}")
print(f"¿Meta exacta? {meta_exacta}")
print(f"¿Diferente a meta? {diferente_meta}")
print(f"¿Menos de la mitad? {menos_de_mitad}\n")

print("Evaluaciones lógicas:")
print(f"¿Situación ideal? {situacion_ideal}")
print(f"¿Situación de riesgo? {situacion_riesgo}")
print(f"¿Situación estable? {situacion_estable}")
print(f"¿Es viable la meta? {es_viable}")
print(f"¿Combinación compleja positiva? {combinacion_compleja}")