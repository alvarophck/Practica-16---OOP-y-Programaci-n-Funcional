class Vehiculo:
    def __init__(self, marca, modelo, anio, velocidad_max):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad_max = velocidad_max

    def mostrar_informacion(self):
        print(f"{self.marca} {self.modelo} ({self.anio})")
        print(f"  Velocidad máxima: {self.velocidad_max} km/h")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, velocidad_max, num_puertas, combustible):
        Vehiculo.__init__(self, marca, modelo, anio, velocidad_max)
        self.num_puertas = num_puertas
        self.combustible = combustible

    def mostrar_informacion(self):
        print("Tipo: Coche")
        Vehiculo.mostrar_informacion(self)
        print(f"  Puertas: {self.num_puertas}")
        print(f"  Combustible: {self.combustible}")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, velocidad_max, cilindrada, tipo_moto):
        Vehiculo.__init__(self, marca, modelo, anio, velocidad_max)
        self.cilindrada = cilindrada
        self.tipo_moto = tipo_moto

    def mostrar_informacion(self):
        print("Tipo: Moto")
        Vehiculo.mostrar_informacion(self)
        print(f"  Cilindrada: {self.cilindrada} cc")
        print(f"  Tipo de moto: {self.tipo_moto}")


class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, velocidad_max, carga_max_kg, num_ejes):
        Vehiculo.__init__(self, marca, modelo, anio, velocidad_max)
        self.carga_max_kg = carga_max_kg
        self.num_ejes = num_ejes

    def mostrar_informacion(self):
        print("Tipo: Camión")
        Vehiculo.mostrar_informacion(self)
        print(f"  Carga máxima: {self.carga_max_kg} kg")
        print(f"  Ejes: {self.num_ejes}")


class Autobus(Vehiculo):
    def __init__(self, marca, modelo, anio, velocidad_max, num_plazas, doble_piso):
        Vehiculo.__init__(self, marca, modelo, anio, velocidad_max)
        self.num_plazas = num_plazas
        self.doble_piso = doble_piso

    def mostrar_informacion(self):
        print("Tipo: Autobús")
        Vehiculo.mostrar_informacion(self)
        print(f"  Plazas: {self.num_plazas}")
        print(f"  Doble piso: {'sí' if self.doble_piso else 'no'}")


coche = Coche("Seat", "León", 2022, 220, 5, "gasolina")
moto = Moto("Yamaha", "MT-07", 2021, 210, 689, "naked")
camion = Camion("Volvo", "FH16", 2020, 90, 18000, 3)
autobus = Autobus("Mercedes", "Citaro", 2019, 85, 60, False)

for vehiculo in [coche, moto, camion, autobus]:
    vehiculo.mostrar_informacion()
    print()
