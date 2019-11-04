

class Cartera:

    def __init__(self):
        self.__tipo = ""
        self.__color = ""
        self.__marca = ""

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setColor(self, color):
        self.__color = color

    def setMarca(self, marca):
        self.__marca = marca

    def getTipo(self):
        return self.__tipo

    def getColor(self):
        return self.__color

    def getMarca(self):
        return self.__marca

    def validateTipo(self):
        tipo = ("Sobre", "Tote" ,"Bandolera" , "Clutch", "Estructurada")
        print("Talla: ")
        tempIndex = input("Elija el tipo de cartera:\n1. Sobre\n2. Tote\n3. Bandolera\n4. Clutch\n5. Estructurada\n")
        while tempIndex not in ("1", "2", "3", "4", "5"):
            print("Entrada incorrecta, por favor intente nuevamente.")
            tempIndex = input("Elija el tipo de cartera:\n1. Sobre\n2. Tote\n3. Bandolera\n4. Clutch\n5. Estructurada\n")
        return tipo[int(tempIndex) - 1]

    def validateMarca(self):
        marca = ("Chanel", "Gucci" ,"SalvatoreFerragamo:" , "Prada", "LouisVuitton")
        print("Marca: ")
        tempIndex = input("Elija la marca:\n1. Chanel\n2. Gucci\n3. SalvatoreFerragamo\n4. Prada\n5. LouisVuitton\n")
        while tempIndex not in ("1", "2", "3", "4" , "5" ):
            print("Entrada incorrecta, por favor intente nuevamente.")
            tempIndex = input("Elija la marca:\n1. Chanel\n2. Gucci\n3. SalvatoreFerragamo\n4. Prada\n5. LouisVuitton\n")
        return marca[int(tempIndex) - 1]
