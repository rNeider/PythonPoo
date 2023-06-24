class Animal:
    #Atributos
    nombre=""#Atributo Estatico
    edad=0
    #Metodos
    def __init__(self,nombre1,edad1):
        self.nombre=nombre1
        self.edad=edad1
        
    #Metodos propios de la clase
    def registrarAnimal(self):
        self.nombre=input("ingre el nombre de el animal")
        self.edad=int(input("ingre la edad de el animal"))
    
    def mostrarAnimal(self):
        print("El animal se llama",self.nombre,"y tiene",self.edad)
        
    #duplicar edad pedir edad , retornar la edad duplicada
    def duplicarEdad(self,edad):
        asd=edad*2
        return asd
        

    def cambiarNombre(self):
        nombre1=input("Dijite el nuevo nombre de el animal")
        self.nombre=nombre1
        print("el nuevo nombre es",self.nombre)
        
        



"""crear un objeto o instanciar la clase
tigre=Animal()

tigre.edad=5
tigre.nombre="Calostro"
print("El nombre de el animal es ",tigre.nombre," y su edad es ",tigre.edad)"""

