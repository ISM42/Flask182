listaproductos=[] 
class almacenBebidas(object): 
    def __init__(self,_id, _nombre, _clasificacion, _marca, _precio): 
        self.id =_id
        self.nombre = _nombre
        self.clasificacion = _clasificacion
        self.marca = _marca
        self.precio= _precio
        self.historial = []
        
    def entregarInformacion(self):
        print("ID: {} - Nombre : {} - Clasificación:  {} - Marca:  {} - Precio : {}".format(self.id, self.nombre, self.clasificacion, self.marca,self.precio))

    def editarRegistro(self,_id, _nombre, _clasificacion, _marca, _precio): 
        self.id = _id
        self.nombre = _nombre
        self.clasificacion = _clasificacion
        self.marca = _marca
        self.precio= _precio
        
        print("Actualizacion realizada")
    def incluirEvento(self,_id, _nombre, _clasificacion, _marca, _precio): 
      
        return("Modificacion: ID: {} - Nombre: {} - Clasificación: {} - Marca: {} - Precio {}".format(_id,_nombre, _clasificacion, _marca, _precio))
    def entregaHistorial(self):
        print("ID: {} - Nombre: {} - Clasificación: {} - Marca: {} - Precio {}".format(self.id, self.nombre, self.clasificacion, self.marca, self.precio))
def registrarProducto():
        id = int(input("Ingresa el ID del producto: "))
        nombre = str(input("Ingresa el nombre del producto: ")) 
        clasificacion = str (input("Ingresa la clasificación del producto: "))
        marca = str(input("Ingresa la marca del producto: "))
        precio = float(input("Ingresa el precio del producto: "))
        objBebida = almacenBebidas(id, nombre, clasificacion, marca, precio)
        listaproductos.append(objBebida) 
def mostraralmacenBebidas(): 
        print("Lista de productos")
        for objBebida in listaproductos: 
            objBebida.entregarInformacion() 
def buscaralmacenBebidas(): 
    print("Buscar productos")
    id = int(input("Ingresa el ID del producto a buscar:")) 
    for objBebida in listaproductos: 
        if id ==objBebida.id:
            objBebida.entregarInformacion() 
def modificarBebida():
    print("Modificar bebida")
    id = int(input("Ingresa el ID del producto a modificar: "))
    for objBebida in listaproductos: 
        if id == objBebida.id:  
            id = int(input("Ingresa el nuevo ID: ")) 
            nombre = str(input("Ingresa el nuevo nombre: ")) 
            clasificacion = str(input("Ingresa la nueva clasificación :")) 
            marca = str(input("Ingresa la nueva marca del producto: "))
            precio = float(input("Ingresa el nuevo precio del producto: "))
            objBebida.editarRegistro(id,nombre,clasificacion,marca,precio)
            objBebida.entregarInformacion()
            recepcionMensaje = objBebida.incluirEvento(id,nombre,clasificacion,marca,precio)
            objBebida.historial.append(recepcionMensaje)
def consultaHistorial():
    print("Consulta de historial del producto")
    id = int(input("Ingresa el ID del producto a consultar: "))
    for objBebida in listaproductos: 
        if id == objBebida.id: 
            for recepcionMensaje in objBebida.historial:
                print("Evento : {}".format(recepcionMensaje)) 

def eliminarRegistro():
    id= print(input("Ingrese el ID del producto que desea eliminar: "))
    bebida=None 

    for objBebida in listaproductos:
        if objBebida.id == id:
            bebida=objBebida
            break
        if bebida:
            listaproductos.remove(bebida)
            print("Registro eliminado correctamente")

        else:
            print("No se encontró el registro ingresado.")


def promedioBebida():
    total=sum(almacenBebidas.precio for almacenBebidas in listaproductos)
    promedio=total/len(listaproductos)
    print(f"El precio promedio de las bebidas es: {promedio}")

def cantClasificacion():
    clasificacion = input("Ingrese la clasificación de la que desea obtener el conteo: ")
    cantidad = sum(1 for almacenBebidas in listaproductos if almacenBebidas.clasificacion == clasificacion)
    print(f"La cantidad de bebidas de la clasificación solicitada es:  {cantidad}")

def cantMarca():
     marca=input("Ingrese el nombre de la marca que desea conocer: ")
     cantidad = sum (1 for almacenBebidas in listaproductos if almacenBebidas.marca == marca)
     print(f"La cantidad de bebidas de la marca solicitada es: {cantidad}")  

def salir():
    print("Salir del programa")
    exit()


def main():  #main es el metodo principal donde uniremos todos los metodos para que realice diferentes funciones
        while True:
            print("             MENU          ")
            print("1.- Registrar un producto nuevo")
            print("2.- Mostrar lista de productos")
            print("3.- Buscar producto")
            print("4.- Editar registro")
            print("5.- Precio promedio por bebida")
            print("6.- Cantidad de bebidas por clasificación")
            print("7.- Cantidad de bebidas por marca")
            print("8.- Eliminar registro")
            print("9.- Mostrar Historial de producto")
            print(" PRESIONE 0 PARA SALIR")
           
            opcion = int(input("Opcion: "))

            if opcion == 1:
                registrarProducto()
            elif opcion == 2:
                mostraralmacenBebidas()
            elif opcion == 3:
                buscaralmacenBebidas()
            elif opcion == 4:
                modificarBebida()
            elif opcion == 5:
                promedioBebida()
            elif opcion == 6:
                cantClasificacion()
            elif opcion == 7:
                cantMarca()    
            elif opcion == 8:
                eliminarRegistro()            
            elif opcion == 9:
                consultaHistorial()
            elif opcion == 0:
                salir()

if __name__ == '__main__':
    main()