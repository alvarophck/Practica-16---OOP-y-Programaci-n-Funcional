class Envio:
    COSTE_POR_KG = 2.0

    def __init__(self, envio_id, destino, peso):
        self.envio_id = envio_id
        self.destino = destino
        self.peso = peso

    def calcular_coste(self):
        return self.peso * self.COSTE_POR_KG

    def mostrar_informacion(self):
        return f"Envío {self.envio_id} a {self.destino} ({self.peso} kg)"


class EnvioNacional(Envio):
    RECARGO = 3

    def calcular_coste(self):
        return super().calcular_coste() + self.RECARGO


class EnvioInternacional(Envio):
    RECARGO = 15

    def calcular_coste(self):
        return super().calcular_coste() + self.RECARGO


class EnvioUrgente(Envio):
    MULTIPLICADOR = 1.5

    def calcular_coste(self):
        return super().calcular_coste() * self.MULTIPLICADOR


envios = [
    EnvioNacional("E01", "Madrid", 2),
    EnvioInternacional("E02", "París", 3),
    EnvioUrgente("E03", "Sevilla", 4),
    EnvioNacional("E04", "Valencia", 5),
    EnvioInternacional("E05", "Roma", 1),
    EnvioUrgente("E06", "Bilbao", 2),
    EnvioNacional("E07", "Málaga", 1),
]

# Parte B: la misma llamada envio.calcular_coste() en todos los objetos.
# Se ejecuta una versión distinta porque Python busca el método en la clase real del
# objeto (EnvioNacional, EnvioInternacional o EnvioUrgente) y usa la versión sobrescrita
# que encuentra allí, no la de la superclase Envio. Eso es el polimorfismo.
for envio in envios:
    print(f"{envio.envio_id}: {envio.calcular_coste()} €")
print()

# Parte C: comprehensions
LIMITE_CARO = 12
envios_caros = [e.envio_id for e in envios if e.calcular_coste() >= LIMITE_CARO]
tipos_envio = {type(e).__name__ for e in envios}
costes_por_envio = {e.envio_id: e.calcular_coste() for e in envios}


# Parte D: programación funcional
def aplicar_operacion(funcion, valor):
    return funcion(valor)


def redondear_euros(importe):
    return round(importe, 2)


def crear_descuento(porcentaje):
    def aplicar(importe):
        return importe * (1 - porcentaje / 100)
    return aplicar


print(aplicar_operacion(redondear_euros, 12.345))
descontar_10 = crear_descuento(10)
print(descontar_10(100))
print()

costes_con_descuento = {
    envio_id: aplicar_operacion(redondear_euros, aplicar_operacion(descontar_10, coste))
    for envio_id, coste in costes_por_envio.items()
    if coste >= LIMITE_CARO
}

# Parte E: informe final
print("Envíos caros:", envios_caros)
print("Tipos de envío:", sorted(tipos_envio))
print("Costes por envío:", costes_por_envio)
print("Costes con descuento:", costes_con_descuento)
