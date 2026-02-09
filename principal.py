from Libro_modelo import Libro_modelo
from Autores import Autor_modelo
from Libro_bd import base_datos_libro


obj_bd = base_datos_libro()


obj_autor = Autor_modelo("sandra", "ortega","18", "2008","Colombiana" )
lista_datos_autor=["carolina","Ortega", "08/04/2008", "Argentina" ]
lista_datos_autor1=["Thomas", "Blanco", "22/02/2007", "Colombiano" ]
print(obj_autor.ver_info())

obj_libro1 = Libro_modelo("2024-01-01", 250, "Aventura", "Ficción")
obj_libro2 = Libro_modelo("2023-05-15", 300, "Ciencia", "No Ficción")
obj_libro3 = Libro_modelo("2022-11-20", 150, "Historia", "Ficción")

obj_bd.guardar_libro(obj_libro1)
obj_bd.guardar_libro(obj_libro2)
obj_bd.guardar_libro(obj_libro3)



obj_bd.remover_libros(obj_libro1)
obj_bd.mostrar_info()