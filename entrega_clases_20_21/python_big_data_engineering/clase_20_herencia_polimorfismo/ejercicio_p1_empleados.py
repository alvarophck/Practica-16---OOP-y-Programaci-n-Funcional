class Empleado:
    def __init__(self, id_empleado, nombre, salario_base, departamento):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.salario_base = salario_base
        self.departamento = departamento

    def mostrar_informacion(self):
        print(f"ID: {self.id_empleado}")
        print(f"Nombre: {self.nombre}")
        print(f"Departamento: {self.departamento}")
        print(f"Salario base: {self.salario_base} €")


class Desarrollador(Empleado):
    def __init__(self, id_empleado, nombre, salario_base, departamento,
                 lenguaje_principal, nivel):
        Empleado.__init__(self, id_empleado, nombre, salario_base, departamento)
        self.lenguaje_principal = lenguaje_principal
        self.nivel = nivel

    def mostrar_informacion(self):
        Empleado.mostrar_informacion(self)
        print(f"Lenguaje principal: {self.lenguaje_principal}")
        print(f"Nivel: {self.nivel}")


class AnalistaDatos(Empleado):
    def __init__(self, id_empleado, nombre, salario_base, departamento,
                 herramienta_bi, especialidad):
        Empleado.__init__(self, id_empleado, nombre, salario_base, departamento)
        self.herramienta_bi = herramienta_bi
        self.especialidad = especialidad

    def mostrar_informacion(self):
        Empleado.mostrar_informacion(self)
        print(f"Herramienta BI: {self.herramienta_bi}")
        print(f"Especialidad: {self.especialidad}")


class AdministradorSistemas(Empleado):
    def __init__(self, id_empleado, nombre, salario_base, departamento,
                 sistema_operativo, certificacion):
        Empleado.__init__(self, id_empleado, nombre, salario_base, departamento)
        self.sistema_operativo = sistema_operativo
        self.certificacion = certificacion

    def mostrar_informacion(self):
        Empleado.mostrar_informacion(self)
        print(f"Sistema operativo: {self.sistema_operativo}")
        print(f"Certificación: {self.certificacion}")


empleados = [
    Desarrollador("E001", "Ana López", 2800, "Desarrollo", "Python", "Senior"),
    Desarrollador("E004", "Mario Ruiz", 2200, "Desarrollo", "Java", "Junior"),
    AnalistaDatos("E002", "Carlos Pérez", 2600, "Datos", "Power BI", "Análisis de ventas"),
    AnalistaDatos("E005", "Elena Marín", 2750, "Datos", "Tableau", "Calidad de datos"),
    AdministradorSistemas("E003", "Laura Gómez", 2900, "Infraestructura", "Linux", "AZ-104"),
    AdministradorSistemas("E006", "Jorge Díaz", 2500, "Infraestructura", "Windows Server", "MS-102"),
]

for empleado in empleados:
    empleado.mostrar_informacion()
    print()
