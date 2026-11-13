from functools import reduce

IVA = 0.21
UMBRAL_ALTO = 200

pedidos = [
    {"pedido_id": "P001", "cliente": "Ana", "importe": 120.0, "estado": "completado"},
    {"pedido_id": "P002", "cliente": "Luis", "importe": 80.0, "estado": "pendiente"},
    {"pedido_id": "P003", "cliente": "Marta", "importe": 250.0, "estado": "completado"},
    {"pedido_id": "P004", "cliente": "Pedro", "importe": 60.0, "estado": "cancelado"},
    {"pedido_id": "P005", "cliente": "Lucía", "importe": 150.0, "estado": "completado"},
]

# 1. Filtrado
completados = list(filter(lambda p: p["estado"] == "completado", pedidos))

# 2. Transformación (sin modificar los diccionarios originales)
con_iva = list(map(
    lambda p: {
        "pedido_id": p["pedido_id"],
        "cliente": p["cliente"],
        "importe_final": round(p["importe"] * (1 + IVA), 2),
    },
    completados,
))

# 3. Acumulación
facturacion_total = round(reduce(lambda acumulado, p: acumulado + p["importe_final"], con_iva, 0), 2)

# 4. Clasificación con una lambda independiente
clasificar = lambda importe: "Alto" if importe >= UMBRAL_ALTO else "Normal"
clasificaciones = list(map(clasificar, [p["importe_final"] for p in con_iva]))

# 5. Presentación
print("Pedidos completados:")
for p in completados:
    print(" ", p)
print("Pedidos transformados:")
for p in con_iva:
    print(" ", p)
print("Clasificaciones:", clasificaciones)
print(f"Facturación total: {facturacion_total:.2f} €")
print()
print("Comprobaciones")
print("3 pedidos completados:", len(completados) == 3)
print("Importes finales:", [p["importe_final"] for p in con_iva] == [145.2, 302.5, 181.5])
print("Total 629.20 €:", facturacion_total == 629.2)
print("Clasificaciones:", clasificaciones == ["Normal", "Alto", "Normal"])
print("Lista original intacta:", pedidos[0] == {"pedido_id": "P001", "cliente": "Ana", "importe": 120.0, "estado": "completado"})
