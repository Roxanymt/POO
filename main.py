from Persona import Persona  #from 'NOMBRE-ARCHIVO' import 'NOMBRE-CLASE'
from Estudiante import Estudiante

#Instancia = el objeto
bonnie = Persona("Bonnie","Montenegro","bonnie@codingdojo.com",30,"Bootcamp Python")
roxany = Persona("Roxany","Montenegro","roxany@codingdojo.com",26,"Bootcamp Python")

print(bonnie.nombre)
print(roxany.nombre)

roxany.cumpleaños()

print(bonnie.edad)
print(roxany.edad)

print(bonnie.lineas_codigo)
print(roxany.lineas_codigo)

bonnie.codificar(45)
print(bonnie.lineas_codigo)

print(bonnie.pais)
print(roxany.pais)

Persona.pais = "México" #se modifica atributo. "clase"."atributo" = "nuevo valor"
print(roxany.pais)

Persona.imprime_lista()

pablo = Persona("Pablo","Picasso","pablo@codingdojo.com",50,"Bootcamp Python")

Persona.imprime_lista()
bonnie.cumpleaños()

bonnie.tomar_cerveza()

pablo.codificar(120)

bonnie.curso.agrega_calificacion(9) #al curso de elena se le agrega calificación
bonnie.curso.agrega_calificacion(7)

print(bonnie.curso.calificaciones)

pedro = Estudiante("Pedro","Páramo","pedro@codingdojo.com", 30, "Bootcampt Python",1234)

print(pedro.email)
print(pedro.id)

pedro.codificar(100) #tambien s heredan los métodos y funciones 
print(pedro.lineas_codigo)

pedro.cumpleaños()

Persona.imprime_lista()

Estudiante.imprime_lista()

bonnie.que_haces()
pedro.que_haces()
