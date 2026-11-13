from functools import reduce

UMBRAL_LENTO_MIN = 25
SEGUNDOS_POR_MINUTO = 60

ejecuciones = [
    {"pipeline": "ventas", "duracion_min": 18, "registros": 12000, "estado": "ok"},
    {"pipeline": "clientes", "duracion_min": 32, "registros": 8000, "estado": "ok"},
    {"pipeline": "inventario", "duracion_min": 12, "registros": 0, "estado": "error"},
    {"pipeline": "facturas", "duracion_min": 45, "registros": 15000, "estado": "ok"},
    {"pipeline": "devoluciones", "duracion_min": 26, "registros": 4000, "estado": "ok"},
    {"pipeline": "proveedores", "duracion_min": 15, "registros": 0, "estado": "error"},
]

# 1. Ejecuciones exitosas
exitosas = list(filter(lambda e: e["estado"] == "ok", ejecuciones))

# 2. Ejecuciones lentas (sobre las exitosas)
lentas = list(filter(lambda e: e["duracion_min"] > UMBRAL_LENTO_MIN, exitosas))

# 3. Transformación
transformadas = list(map(
    lambda e: {
        "pipeline": e["pipeline"],
        "duracion_min": e["duracion_min"],
        "duracion_seg": e["duracion_min"] * SEGUNDOS_POR_MINUTO,
        "registros": e["registros"],
    },
    exitosas,
))

# 4. Total de registros procesados
total_registros = reduce(lambda acumulado, e: acumulado + e["registros"], exitosas, 0)

# 5. Tiempo total de procesamiento
tiempo_total = reduce(lambda acumulado, e: acumulado + e["duracion_min"], exitosas, 0)

# 6. Ordenación de mayor a menor duración
ordenadas = sorted(exitosas, key=lambda e: e["duracion_min"], reverse=True)

# 7. Informe final
print("Ejecuciones exitosas:", len(exitosas))
print("Pipelines lentos:", [e["pipeline"] for e in lentas])
print("Lista transformada:")
for e in transformadas:
    print(" ", e)
print("Total de registros:", total_registros)
print("Tiempo acumulado:", tiempo_total, "minutos")
print("Orden por duración:", [e["pipeline"] for e in ordenadas])
print()
print("Comprobaciones")
print("4 ejecuciones exitosas:", len(exitosas) == 4)
print("Lentos:", [e["pipeline"] for e in lentas] == ["clientes", "facturas", "devoluciones"])
print("39000 registros:", total_registros == 39000)
print("121 minutos:", tiempo_total == 121)
print("Orden:", [e["pipeline"] for e in ordenadas] == ["facturas", "clientes", "devoluciones", "ventas"])
print("Lista original intacta:", len(ejecuciones) == 6 and "duracion_seg" not in ejecuciones[0])
