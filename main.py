from Persona import Persona  #from 'NOMBRE-ARCHIVO' import 'NOMBRE-CLASE'

#Instancia = el objeto
bonnie = Persona("Bonnie","Montenegro","bonnie@codingdojo.com",30)
roxany = Persona("Roxany","Montenegro","roxany@codingdojo.com",26)

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

pablo = Persona("Pablo","Picasso","pablo@codingdojo.com",50)

Persona.imprime_lista()
bonnie.cumpleaños()

bonnie.tomar_cerveza()

pablo.codificar(120)

bonnie.curso.agrega_calificacion(9) #al curso de elena se le agrega calificación
bonnie.curso.agrega_calificacion(7)

print(bonnie.curso.calificaciones)