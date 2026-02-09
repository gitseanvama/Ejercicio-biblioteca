class Autor_modelo:
    def __init__(self, dato_nombre, dato_apellido, dato_edad, dato_año, dato_pais):
        self.nombre = dato_nombre
        self.apellido = dato_apellido
        self.edad = dato_edad
        self.año = dato_año
        self.pais = dato_pais


    def regsitrar_datos(self):
        mensaje = " se registraron los datos"
        return mensaje

    def buscar_autor(self, dato_buscar):
        mensaje = "autor existe en la base de datos" + dato_buscar
        return mensaje

    def dar_baja_autor(self, dato):
        mensaje = "el autor esta inactivo" + dato
        return mensaje

    def ver_info(self):
        print(f"nombre: {self.nombre} - apellido: {self.apellido} - edad: {self.edad} - año: {self.año} - pais: {self.pais}")