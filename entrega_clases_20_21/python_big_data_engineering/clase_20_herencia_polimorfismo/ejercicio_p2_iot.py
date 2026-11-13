class DispositivoIoT:
    def __init__(self, device_id, nombre, ubicacion, valor, unidad):
        self.device_id = device_id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.valor = valor
        self.unidad = unidad

    def mostrar_informacion(self):
        print("ID:", self.device_id)
        print("Nombre:", self.nombre)
        print("Ubicación:", self.ubicacion)
        print("Valor:", self.valor, self.unidad)


class SensorHumedad(DispositivoIoT):
    def __init__(self, device_id, nombre, ubicacion, valor, unidad, profundidad, calibracion):
        DispositivoIoT.__init__(self, device_id, nombre, ubicacion, valor, unidad)
        self.profundidad = profundidad
        self.calibracion = calibracion

    def mostrar_informacion(self):
        DispositivoIoT.mostrar_informacion(self)
        print("Profundidad:", self.profundidad, "cm")
        print("Calibración:", self.calibracion)


class SensorTemperatura(DispositivoIoT):
    def __init__(self, device_id, nombre, ubicacion, valor, unidad, altitud, precision):
        DispositivoIoT.__init__(self, device_id, nombre, ubicacion, valor, unidad)
        self.altitud = altitud
        self.precision = precision

    def mostrar_informacion(self):
        DispositivoIoT.mostrar_informacion(self)
        print("Altitud:", self.altitud, "m")
        print("Precisión:", self.precision, "°C")


class SensorViento(DispositivoIoT):
    def __init__(self, device_id, nombre, ubicacion, valor, unidad, orientacion, velocidad_maxima):
        DispositivoIoT.__init__(self, device_id, nombre, ubicacion, valor, unidad)
        self.orientacion = orientacion
        self.velocidad_maxima = velocidad_maxima

    def mostrar_informacion(self):
        DispositivoIoT.mostrar_informacion(self)
        print("Orientación:", self.orientacion)
        print("Velocidad máxima:", self.velocidad_maxima, "km/h")


class SensorTanque(DispositivoIoT):
    def __init__(self, device_id, nombre, ubicacion, valor, unidad, capacidad, nivel_bateria):
        DispositivoIoT.__init__(self, device_id, nombre, ubicacion, valor, unidad)
        self.capacidad = capacidad
        self.nivel_bateria = nivel_bateria

    def mostrar_informacion(self):
        DispositivoIoT.mostrar_informacion(self)
        print("Capacidad:", self.capacidad, "L")
        print("Nivel de batería:", self.nivel_bateria, "%")


def categoria(dispositivo):
    if isinstance(dispositivo, SensorHumedad):
        return "Sensor de humedad"
    if isinstance(dispositivo, SensorTemperatura):
        return "Sensor de temperatura"
    if isinstance(dispositivo, SensorViento):
        return "Sensor de viento"
    if isinstance(dispositivo, SensorTanque):
        return "Sensor de tanque"
    return "Dispositivo genérico"


dispositivos = [
    SensorHumedad("DEV001", "Sensor de suelo", "Parcela A", 45, "%", 30, "Automática"),
    SensorTemperatura("DEV002", "Sensor ambiental", "Parcela B", 26, "°C", 650, 0.5),
    SensorViento("DEV003", "Anemómetro", "Parcela C", 18, "km/h", "Norte", 80),
    SensorTanque("DEV004", "Tanque principal", "Parcela A", 75, "%", 5000, 90),
    SensorHumedad("DEV005", "Sensor de raíz", "Parcela B", 38, "%", 50, "Manual"),
    SensorTemperatura("DEV006", "Sensor de invernadero", "Parcela C", 31, "°C", 640, 0.2),
    SensorViento("DEV007", "Anemómetro de lindero", "Parcela A", 22, "km/h", "Sur", 95),
    SensorTanque("DEV008", "Tanque de riego", "Parcela B", 40, "%", 2500, 72),
]

for dispositivo in dispositivos:
    dispositivo.mostrar_informacion()
    print("Categoría:", categoria(dispositivo))
    print("-" * 40)

print("Atributos de cada objeto (vars):")
for dispositivo in dispositivos:
    print(dispositivo.device_id, vars(dispositivo))
