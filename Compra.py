from Cartera import Cartera
from Vestido import Vestido
from Pantalon import Pantalon
from Remera import Remera
from Cliente import Cliente

class Compra(Cartera, Vestido, Pantalon, Remera, Cliente):
    def __init__(self):
        self.__compras = []
        self.__cliente = []

    def updateCompra(self, nuevaCompra):
        self.__compras.append(nuevaCompra)

    def updateCliente(self, nuevoCliente):
        self.__cliente.append(nuevoCliente)

    def getCompra(self):
        return self.__compras

    def getClientes(self):
        return self.__cliente

    def mostrarCompras(self):
        if not self.__compras:
            print("No hay ninguna compra creada.")
        for x in range(len(self.__compras)):
            print("\nProducto ", x + 1, ":\n")
            if type(self.__compras[x]) == Vestido:
                print("Producto: Vestido")
                print("Color:", self.__compras[x].getColor(), "\nSize:", self.__compras[x].getSize(), "\nMarca:"
                      , self.__compras[x].getMarca())
            elif type(self.__compras[x]) == Cartera:
                print("Producto: Cartera")
                print("Color:", self.__compras[x].getColor(), "\nTipo:", self.__compras[x].getTipo(), "\nMarca:"
                      , self.__compras[x].getMarca())
            elif type(self.__compras[x]) == Pantalon:
                print("Producto: Pantalon")
                print("Color:", self.__compras[x].getColor(), "\nSize:", self.__compras[x].getSize(), "\nMarca:"
                      , self.__compras[x].getMarca())
            else:
                print("Producto: Remera")
                print("Color:", self.__compras[x].getColor(), "\nSize:", self.__compras[x].getSize(), "\nMarca:"
                      , self.__compras[x].getMarca())

    def contarCompras(self):
        return print("\n", len(self.__compras), "Compras.")

    def mostrarClientes(self):
        if not self.__cliente:
            print("No hay clientes creados")
        for x in range(len(self.__cliente)):
            print("\nCliente:", x + 1, "\n")
            print("Nombre:", self.__cliente[x].getNombre(), "\nApellido:", self.__cliente[x].getApellido(), "\nTelefono:", self.__cliente[x].getTelefono(), "\nEmail:", self.__cliente[x].getEmail(), "\nDNI:", self.__cliente[x].getDni())

    def borrarCompras(self):
        if not self.__compras:
            print("No hay compras.")
            return
        print("Las compras son:")
        for x, y in enumerate(self.__compras):
            print(x + 1, ".", y.getMarca())
        print("Seleccione que compra desea borrar ('0' para salir).")
        tempIndex = 0
        while not tempIndex:
            try:
                tempIndex = int(input())
                if tempIndex == 0:
                    return
            except ValueError:
                print("Entrada inválida,por favor intente de nuevo")
            if not 1 <= tempIndex <= len(self.__compras):
                print("Valor ingresado fuera del rango de la lista de compras.")
                tempIndex = 0
        self.__compras.pop(tempIndex - 1)

    def borrarClientes(self):
        if not self.__cliente:
            print("No hay clientes ingresados.")
            return
        print("Los clientes ingresados son:")
        for x, y in enumerate(self.__cliente):
            print(x + 1, ".", y.getNombre())
        print("Seleccione que cliente desea borrar ('0' para salir).")
        tempIndex = 0
        while not tempIndex:
            try:
                tempIndex = int(input())
                if tempIndex == 0:
                    return
            except ValueError:
                print("Entrada inválida,por favor intenta de nuevo.")
            if not 1 <= tempIndex <= len(self.__cliente):
                print("Valor ingresado fuera del rango de la lista de clientes.")
                tempIndex = 0
        self.__cliente.pop(tempIndex - 1)
