class Cliente:
    def __init__(self):
        self.__nombre = ""
        self.__apellido = ""
        self.__telefono = ""
        self.__email = ""
        self.__dni = ""

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def setEmail(self, email):
        self.__email = email

    def setDni(self, dni):
        self.__dni = dni

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getTelefono(self):
        return self.__telefono

    def getEmail(self):
        return self.__email

    def getDni(self):
        return self.__dni

