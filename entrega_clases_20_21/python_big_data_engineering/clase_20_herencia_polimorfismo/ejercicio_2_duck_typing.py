# Ejemplo 1: clases sin relación entre sí que comparten el método exportar()

class ExportadorCSV:
    def exportar(self, filas):
        print("Exportando a CSV:")
        for fila in filas:
            print("  " + ",".join([str(valor) for valor in fila]))


class ExportadorJSON:
    def exportar(self, filas):
        print("Exportando a JSON:")
        print("  [" + ", ".join([str(list(fila)) for fila in filas]) + "]")


class ExportadorLog:
    def exportar(self, filas):
        print(f"Registrando {len(filas)} filas en el log")


class Impresora:
    pass


def guardar(destino, filas):
    destino.exportar(filas)


filas = [("ventas", 120), ("clientes", 45), ("stock", 300)]
for destino in [ExportadorCSV(), ExportadorJSON(), ExportadorLog()]:
    guardar(destino, filas)

try:
    guardar(Impresora(), filas)
except AttributeError as error:
    print("Error:", error)

print("-" * 40)

# Ejemplo 2: duck typing con protocolos (__len__ y __iter__)

class LoteVentas:
    def __init__(self, importes):
        self.importes = importes

    def __len__(self):
        return len(self.importes)

    def __iter__(self):
        return iter(self.importes)


def resumen(coleccion):
    total = 0
    for importe in coleccion:
        total += importe
    return f"{len(coleccion)} elementos, total {total}"


print(resumen([10, 20, 30]))
print(resumen((5, 15)))
print(resumen(LoteVentas([100, 250, 50, 75])))
print(resumen(range(1, 5)))

try:
    print(resumen(42))
except TypeError as error:
    print("Error:", error)
