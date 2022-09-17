from Curso import Curso
class Persona:
    
    pais = "Chile" #atributo de toda la clase
    lista_personas= [] #lista de todas las instancias 
    total_lineas_codigo = 0 #total de lineas de codigo de todos

    def __init__(self, nombre, apellido, email, edad, nombre_curso): #a través de init se inicializa la instancia. SELF incluye toda la información del objeto.
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad
        self.lineas_codigo = 0
        Persona.lista_personas.append(self)
        self.curso = Curso(nombre_curso)

    #métodos para instancais en especifico
    def cumpleaños(self): #está a la misma altura de init
        self.edad += 1
        print("¡Muchas felicidades!")
        if Persona.mayoria_edad(self.edad):
            print("Wujuu, eres mayor de edad")


    def codificar(self, abc):
        #self.lineas_codigo += cantidad_lineas
        self.lineas_codigo += abc
        Persona.total_lineas_codigo += abc
        if Persona.experto(self.lineas_codigo):
            print("Eres toda una experta codifcando",self.nombre,"!!!!")


    #método genral que aplica a TODAS la instancia de la clase
    @classmethod #indica que el sig método corresponde a toda la clase 
    def imprime_lista(cls):  #cls = Persona (la clase)
        print("Total de personas:", len (cls.lista_personas))
        for persona in cls.lista_personas:
            print(persona.nombre)

    #método estático, función generica. no aplica especificamente a un objeto. 
    @staticmethod
    def mayoria_edad(edad):
        if edad >= 18:
            return True
        else:
            return False

    @staticmethod
    def experto(lineas): #recibo un numero
        if lineas > 100: #si num es mayor a 100 es experto
            return True
        else:
            return False

    def tomar_cerveza(self): #self = Bonnie
        if Persona.mayoria_edad(self.edad):
            print("Aquí esta tu cerveza",self.nombre)
        else:
            print("Lo siento",self.nombre,", no puedes beber")

    def que_haces(self):
        #raise NotImplementedError #cuando a la persona le preguntan que haces, dirá "nada"
        print("Nada! :)")


