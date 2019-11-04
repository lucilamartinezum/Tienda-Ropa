

class Vestido:

    def __init__(self):
        self.__size = ""
        self.__color = ""
        self.__marca = ""

    def setSize(self, size):
        self.__size = size

    def setColor(self, color):
        self.__color = color

    def setMarca(self, marca):
        self.__marca = marca

    def getSize(self):
        return self.__size

    def getColor(self):
        return self.__color

    def getMarca(self):
        return self.__marca

    def validateSize(self):
        size = ("Uno", "Dos" ,"Tres" , "Cuatro")
        print("Talla: ")
        tempIndex = input("Elija tamaño:\n1. Uno\n2. Dos\n3. Tres\n4. Cuatro\n")
        while tempIndex not in ("1", "2", "3", "4"):
            print("Entrada incorrecta, por favor intente nuevamente.")
            tempIndex = input("Elija la talla:\n1. Uno\n2. Dos\n3. Tres\n4. Cuatro\n")
        return size[int(tempIndex) - 1]

    def validateMarca(self):
        marca = ("ChinaByAntolin", "Versace" ,"Benjamina" , "Shibinda", "Bertha", "Dolce&Gabbana")
        print("Marca: ")
        tempIndex = input("Elija la marca:\n1. ChinaByAntolin\n2. Versace\n3. Benjamina\n4. Shibinda\n5. Bertha\n6. Dolce&Gabbana\n")
        while tempIndex not in ("1", "2", "3", "4" , "5" ,"6"):
            print("Entrada incorrecta, por favor intente nuevamente.")
            tempIndex = input("Elija la marca:\n1. ChinaByAntolin\n2. Versace\n3. Benjamina\n4. Shibinda\n5. Bertha\n6. Dolce&Gabbana\n")
        return marca[int(tempIndex) - 1]
