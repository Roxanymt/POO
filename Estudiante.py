from Persona import Persona #Persona es la clase superior

class Estudiante(Persona): #() dice que la clase a heredar es Persona

    lista_estudiantes = []
    #Estudiante
    def __init__(self, nombre, apellido, email, edad, nombre_curso, id): #atributo extra se deba gregar acá también
        super().__init__(nombre, apellido, email, edad, nombre_curso)
        self.id = id #se agrega atributo extra
        Estudiante.lista_estudiantes.append(self)

    @classmethod
    def imprime_lista(cls):
        print("Total de estudiantes:", len(cls.lista_estudiantes))
        for estudiante in cls.lista_estudiantes:
            print(estudiante.nombre)

    def cumpleaños(self):
        super().cumpleaños() #se agrega la funcion del superior, hace lo mismo, y se agrega lo de abajo 
        self.edad += 2
        print("A seguir estudiando!")

    def que_haces(self):
        print("Estoy estudiando en Coding Dojo y aprendiendo muchisimo! :)")