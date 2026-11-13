class ArchivoDatos:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tamaño: {self.tamano} MB")

    def procesar(self):
        print("Procesamiento genérico de archivo")


class ArchivoCSV(ArchivoDatos):
    def procesar(self):
        print(f"Procesando archivo CSV: {self.nombre}")
        print("Leyendo registros separados por comas...")


class ArchivoJSON(ArchivoDatos):
    def procesar(self):
        print(f"Procesando archivo JSON: {self.nombre}")
        print("Extrayendo propiedades de los objetos JSON...")


class ArchivoTXT(ArchivoDatos):
    def procesar(self):
        print(f"Procesando archivo TXT: {self.nombre}")
        print("Leyendo líneas y realizando limpieza básica...")


def ejecutar_procesamiento(archivo):
    archivo.mostrar_informacion()
    archivo.procesar()


archivo1 = ArchivoCSV("ventas.csv", 15)
archivo2 = ArchivoJSON("sensores.json", 8)
archivo3 = ArchivoTXT("logs.txt", 25)

archivos = [archivo1, archivo2, archivo3]
for archivo in archivos:
    ejecutar_procesamiento(archivo)
    print()

# Parte F: nuevo formato sin tocar ejecutar_procesamiento()

class ArchivoXML(ArchivoDatos):
    def procesar(self):
        print(f"Procesando archivo XML: {self.nombre}")
        print("Analizando etiquetas y atributos XML...")


archivos.append(ArchivoXML("configuracion.xml", 3))
print("--- Lista ampliada con el formato XML ---")
print()
for archivo in archivos:
    ejecutar_procesamiento(archivo)
    print()

# Respuestas a las preguntas
#
# 1. Las clases hijas heredan el constructor __init__ (y por tanto los atributos nombre y
#    tamano), mostrar_informacion() y procesar(). Solo procesar() se sobrescribe.
#
# 2. Porque cada formato se procesa de una forma distinta. El método heredado muestra un
#    mensaje genérico, y cada subclase lo sustituye por el comportamiento propio de su formato.
#
# 3. En ejecutar_procesamiento(): la misma llamada archivo.procesar() ejecuta una versión
#    distinta según la clase del objeto recibido.
#
# 4. Porque cada objeto sabe cómo procesarse a sí mismo. La función no necesita averiguar
#    su tipo: se limita a pedirle que ejecute procesar() y Python elige el método de su clase.
#
# 5. Se puede añadir un formato nuevo creando una subclase, sin modificar la función ni el
#    bucle que ya existen. El código anterior sigue funcionando igual y no se corre el riesgo
#    de romperlo al ampliar el sistema.
