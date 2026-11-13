class RecursoComputacional:
    tipo = "Recurso"
    WH_POR_KWH = 1000

    def __init__(self, id_recurso, nombre, fabricante, potencia_w, horas_uso):
        self.id_recurso = id_recurso
        self.nombre = nombre
        self.fabricante = fabricante
        self.potencia_w = potencia_w
        self.horas_uso = horas_uso

    def mostrar_informacion(self):
        print(f"Recurso: {self.id_recurso}")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Fabricante: {self.fabricante}")

    def calcular_consumo(self):
        return (self.potencia_w * self.horas_uso) / self.WH_POR_KWH


class Ordenador(RecursoComputacional):
    tipo = "Ordenador"

    def __init__(self, id_recurso, nombre, fabricante, potencia_w, horas_uso,
                 procesador, ram_gb, sistema_operativo):
        RecursoComputacional.__init__(self, id_recurso, nombre, fabricante, potencia_w, horas_uso)
        self.procesador = procesador
        self.ram_gb = ram_gb
        self.sistema_operativo = sistema_operativo

    def mostrar_informacion(self):
        RecursoComputacional.mostrar_informacion(self)
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram_gb} GB")
        print(f"Sistema operativo: {self.sistema_operativo}")


class Servidor(RecursoComputacional):
    tipo = "Servidor"

    def __init__(self, id_recurso, nombre, fabricante, potencia_w, horas_uso,
                 num_cpu, ram_gb, almacenamiento_tb):
        RecursoComputacional.__init__(self, id_recurso, nombre, fabricante, potencia_w, horas_uso)
        self.num_cpu = num_cpu
        self.ram_gb = ram_gb
        self.almacenamiento_tb = almacenamiento_tb

    def mostrar_informacion(self):
        RecursoComputacional.mostrar_informacion(self)
        print(f"Número de CPU: {self.num_cpu}")
        print(f"RAM: {self.ram_gb} GB")
        print(f"Almacenamiento: {self.almacenamiento_tb} TB")


class DispositivoEdge(RecursoComputacional):
    tipo = "Dispositivo Edge"

    def __init__(self, id_recurso, nombre, fabricante, potencia_w, horas_uso,
                 modelo_gpu, memoria_gpu_gb, tipo_inferencia):
        RecursoComputacional.__init__(self, id_recurso, nombre, fabricante, potencia_w, horas_uso)
        self.modelo_gpu = modelo_gpu
        self.memoria_gpu_gb = memoria_gpu_gb
        self.tipo_inferencia = tipo_inferencia

    def mostrar_informacion(self):
        RecursoComputacional.mostrar_informacion(self)
        print(f"GPU: {self.modelo_gpu}")
        print(f"Memoria GPU: {self.memoria_gpu_gb} GB")
        print(f"Tipo de inferencia: {self.tipo_inferencia}")


recursos = [
    Ordenador("PC-01", "Estación de trabajo 1", "Dell", 250, 50, "Intel Core i7", 32, "Windows 11"),
    Ordenador("PC-02", "Estación de trabajo 2", "Lenovo", 180, 70, "AMD Ryzen 7", 16, "Ubuntu 24.04"),
    Servidor("SRV-01", "Servidor de datos", "HPE", 700, 60, 2, 128, 4),
    Servidor("SRV-02", "Servidor de cómputo", "Dell", 850, 45, 4, 256, 8),
    DispositivoEdge("EDG-01", "Nodo de cámaras", "NVIDIA", 30, 300, "Jetson Orin", 8, "visión artificial"),
    DispositivoEdge("EDG-02", "Nodo de sensores", "NVIDIA", 15, 400, "Jetson Nano", 4, "series temporales"),
]

print("========== LABORATORIO BIG DATA ==========")
consumo_total = 0
mayor = recursos[0]
for recurso in recursos:
    print()
    recurso.mostrar_informacion()
    consumo = recurso.calcular_consumo()
    print(f"Consumo acumulado: {consumo} kWh")
    consumo_total += consumo
    if consumo > mayor.calcular_consumo():
        mayor = recurso

num_ordenadores = sum([1 for r in recursos if isinstance(r, Ordenador)])
num_servidores = sum([1 for r in recursos if isinstance(r, Servidor)])
num_edge = sum([1 for r in recursos if isinstance(r, DispositivoEdge)])

print()
print("========== RESUMEN DEL LABORATORIO ==========")
print()
print("Ordenadores:", num_ordenadores)
print("Servidores:", num_servidores)
print("Dispositivos Edge:", num_edge)
print()
print(f"Consumo total: {round(consumo_total, 2)} kWh")
print("Dispositivo de mayor consumo:", mayor.id_recurso)
