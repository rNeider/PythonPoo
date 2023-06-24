class Persona:
    TipoDoc="DNI"
    documento="1098356243"
    nombre="Neider Huberty"
    apellido="Dulcey Ariza"
    peso="65K"
    estatura="1.76"
    edad="18"
    sexo="Masculino"


    def pedirDatos(self):
        self.__TipoDoc=input("Dijite su tipo de documento")
        self.__documento=int(input("Dijite su numero de documento"))
        self.__nombre=input("Dijite sus nombres completos")
        self.__apellido=input("Dijite sus apellidos")
        self.__peso=float(input("Dijite su peso"))
        self.__estatura=float(input("Dijite su estatura"))
        self.__edad=int(input("Dijite su edad"))
        self.__sexo=input("Dijite su sexo M/F")

    def mostrarPersona(self):
      print("Los datos de la persona ",self.__nombre,"son los siguientes")
      print("Tipo Documento",self.__TipoDoc)
      print("Numero documento",self.__documento)
      print("Nombre",self.__nombre)
      print("Apellido",self.__apellido)
      print("Peso",self.__peso)
      print("Estatura",self.__estatura)
      print("Edad",self.__edad)
      print("Sexo",self.__sexo)
    
    def calcularImc(self):
        imc=self.__peso/(self.__estatura*2)
        if imc<20.0:
            variable="El peso esta por debajo de lo ideal"
        elif imc>=20 and imc<=25.0:
            variable("El peso es ideal")
        elif imc>25.0:
            variable("Usted tiene sobreComida")
        return variable
    
    def mayorEdad(self):
        if self.__edad>=18:
            print("Usted es mayor de edad")
        else:
            print("Usted es menor de edad")
        
      