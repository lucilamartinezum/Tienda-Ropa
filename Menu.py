from Vestido import Vestido
from Cartera import Cartera
from Pantalon import Pantalon
from Remera import Remera
from Cliente import Cliente
from Compra import Compra

def menu():
    nuevaCompra = Compra()
    exitMenu = False
    while not exitMenu:
        print("\n1. Mostrar productos\n2. Crear producto\n3. Borrar producto\n4. Modificar producto\n"
              "5. Mostrar clientes\n6. Crear cliente\n7. Borrar cliente\n8. Modificar cliente\n9. Exit menu")
        select = input(": ")
        if select == "1":
            mostrarCompras(nuevaCompra)
        elif select == "2":
            nuevoProducto = crearCompra()
            if nuevoProducto:
                nuevaCompra.updateCompra(nuevoProducto)
        elif select == "3":
            borrarCompras(nuevaCompra)
        elif select == "4":
            modificarCompra(nuevaCompra.getCompra())
        elif select == "5":
            mostrarClientes(nuevaCompra)
        elif select == "6":
            nuevoCliente = crearCliente()
            if nuevoCliente:
                nuevaCompra.updateCliente(nuevoCliente)
        elif select == "7":
            borrarClientes(nuevaCompra)
        elif select == "8":
            modificarCliente(nuevaCompra.getClientes())
        elif select == "9":
            exitMenu = True
        else:
            print("Entrada inválida")

def mostrarCompras(Compra):
    Compra.mostrarCompras()

def borrarCompras(Compra):
    Compra.borrarCompras()

def crearCompra():
    print("Elija la compra que quiere realizar:\n1. Vestido\n2. Cartera\n3. Pantalon\n4. Remera\n5. Salir de creaacion de compra")
    select = input(": ")
    if select == "1":
        return crearVestido()
    elif select == "2":
        return crearCartera()
    elif select == "3":
        return crearPantalon()
    elif select == "4":
        return crearRemera()
    elif select == "5":
        return
    else:
        print("Numero invalido, intenta de nuevo")

def crearVestido():
    print("Creando producto de 'Vestido'.")
    nuevoProducto = Vestido()
    nuevoProducto.setColor(input("Color: "))
    nuevoProducto.setSize(nuevoProducto.validateSize())
    nuevoProducto.setMarca(nuevoProducto.validateMarca())
    return nuevoProducto

def crearCartera():
    print("Creando producto de 'Cartera'.")
    nuevoProducto = Cartera()
    nuevoProducto.setColor(input("Color: "))
    nuevoProducto.setTipo(nuevoProducto.validateTipo())
    nuevoProducto.setMarca(nuevoProducto.validateMarca())
    return nuevoProducto

def crearPantalon():
    print("Creando producto de 'Pantalon'.")
    nuevoProducto = Pantalon()
    nuevoProducto.setColor(input("Color: "))
    nuevoProducto.setSize(nuevoProducto.validateSize())
    nuevoProducto.setMarca(nuevoProducto.validateMarca())
    return nuevoProducto

def crearRemera():
    print("Creando producto de 'Remera'")
    nuevoProducto = Remera()
    nuevoProducto.setColor(input("Color: "))
    nuevoProducto.setSize(nuevoProducto.validateSize())
    nuevoProducto.setMarca(nuevoProducto.validateMarca())
    return nuevoProducto

def modificarCompra(compras):
    for x, compra in enumerate(compras):
        print(x + 1, ". ", compra.getMarca())
    index = int(input("Ingrese que producto desea modificar: ")) - 1
    while not 0 <= index <= len(compras):
        print("Entrada incorrecta, por favor intente de nuevo")
        index = int(input("Ingrese que producto desea modificar: ")) - 1
    if type(compras[index]) == Vestido:
        modificarVestido(compras[index])
    if type(compras[index]) == Cartera:
        modificarCartera(compras[index])
    if type(compras[index]) == Pantalon:
        modificarPantalon(compras[index])
    if type(compras[index]) == Remera:
        modificarRemera(compras[index])

def modificarVestido(vestido):
    while True:
        print("Producto: Vestido")
        print("1. Color: ", vestido.getColor())
        print("2. Size: ", vestido.getSize())
        print("3. Marca: ", vestido.getMarca())
        print("4. Volver al menú principal ")
        print("Ingrese que atributo desea modificar: ")
        att = input()
        while att not in ("1", "2", "3", "4"):
            print("Entrada inválida, por favor intente de nuevo.")
            att = input("Ingrese que atributo desea modificar: ")
        if att == "1":
            colour = input("Ingrese Color: ")
            vestido.setColor(colour)
        if att == "2":
            vestido.setSize(vestido.validateSize())
        if att == "3":
            vestido.setMarca(vestido.validateMarca())
        if att == "4":
            return

def modificarCartera(cartera):
    while True:
        print("Producto: Cartera")
        print("1. Color: ", cartera.getColor())
        print("2. Tipo: ", cartera.getTipo())
        print("3. Marca: ", cartera.getMarca())
        print("4. Volver al menú principal ")
        print("Ingrese que atributo desea modificar: ")
        att = input()
        while att not in ("1", "2", "3", "4"):
            print("Entrada inválida, por favor intente de nuevo.")
            att = input("Ingrese que atributo desea modificar: ")
        if att == "1":
            colour = input("Ingrese Color: ")
            cartera.setColor(colour)
        if att == "2":
            cartera.setTipo(cartera.validateTipo())
        if att == "3":
            cartera.setMarca(cartera.validateMarca())
        if att== "4":
            return

def modificarPantalon(pantalon):
    while True:
        print("Producto: Pantalon")
        print("1. Color: ", pantalon.getColor())
        print("2. Size: ", pantalon.getSize())
        print("3. Marca: ", pantalon.getMarca())
        print("4. Volver al menú principal ")
        print("Ingrese que atributo desea modificar: ")
        att = input()
        while att not in ("1", "2", "3", "4"):
            print("Entrada inválida, por favor intente de nuevo.")
            att = input("Ingrese que atributo desea modificar: ")
        if att == "1":
            colour = input("Ingrese Color: ")
            pantalon.setColor(colour)
        if att == "2":
            pantalon.setSize(pantalon.validateSize())
        if att == "3":
            pantalon.setMarca(pantalon.validateMarca())
        if att == "4":
            return

def modificarRemera(remera):
    while True:
        print("Producto: Remera")
        print("1. Color: ", remera.getColor())
        print("2. Size: ", remera.getSize())
        print("3. Marca: ", remera.getMarca())
        print("4. Volver al menú principal ")
        print("Ingrese que atributo desea modificar: ")
        att = input()
        while att not in ("1", "2", "3", "4"):
            print("Entrada inválida, por favor intente de nuevo.")
            att = input("Ingrese que atributo desea modificar: ")
        if att == "1":
            colour = input("Ingrese Color: ")
            remera.setColor(colour)
        if att == "2":
            remera.setSize(remera.validateSize())
        if att == "3":
            remera.setMarca(remera.validateMarca())
        if att== "4":
            return

def mostrarClientes(Compra):
    Compra.mostrarClientes()

def crearCliente():
    print("Creando cliente.")
    nuevoCliente = Cliente()
    nuevoCliente.setNombre(input("Nombre: "))
    nuevoCliente.setApellido(input("Apellido: "))
    nuevoCliente.setTelefono(input("Telefono: "))
    nuevoCliente.setEmail(input("Email: "))
    nuevoCliente.setDni(input("DNI: "))
    return nuevoCliente

def borrarClientes(compra):
    compra.borrarClientes()

def modificarCliente(cliente):
    for x, client in enumerate(cliente):
        print(x + 1, ". ", client.getNombre())
    print("Ingrese que cliente desea modificar. ('0' para salir)")
    temp = int(input()) - 1
    while not 0 <= temp <= len(cliente):
        print("Entrada inválida, intente nuevamente")
        print("Ingrese que cliente desea modificar. ('0' para salir)")
        temp = int(input()) - 1
    if temp == 0:

     print("1. Modificar nombre: ", cliente[temp].getNombre(), "\n2. Modificar apellido: ", cliente[temp].getApellido(),"\n3. Modificar telefono: ", cliente[temp].getTelefono(), "\n4. Modificar email: ", cliente[temp].getEmail(), "\n5. Modificar DNI: ", cliente[temp].getDni(),"\n")
    att = input(": ")
    while att not in ("1", "2","3","4","5", "6"):
        print("Entrada inválida,intenta de nuevo")
        att = input(": ")
    if att == "1":
        cliente[temp].setNombre(input("Nombre: "))
    if att == "2":
        cliente[temp].setApellido(input("Apellido: "))
    if att == "3":
        cliente[temp].setTelefono(input("Telefono: "))
    if att == "4":
        cliente[temp].setEmail(input("Email: "))
    if att == "5":
        cliente[temp].setDni(input("DNI: "))
    if att == "6":
        return

