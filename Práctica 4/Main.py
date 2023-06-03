listaproductos=[]
class almacenBebidas(object): 
    def __init__(self,_id,_nombre,_precio,_clasificacion,_marca): 
        self.id = _id
        self.nombre = _nombre
        self.precio = _precio
        self.clasificacion = _clasificacion
        self.marca = _marca
        
    def DarAlta(self): 
        print("ID: {} -{} -{} -{} -{}".format(self.id,self.nombre,self.precio,self.clasificacion,self.marca))
        
    def DarBaja(self,_id): 
        self.id = _id
        print("Producto eliminado exitosamente")

    
    def Actualizar(self,_id,_nombre,_precio,_clasificacion,_marca):
        self.id = _id
        self.nombre = _nombre
        self.precio = _precio
        self.clasificacion = _clasificacion
        self.marca = _marca
        print("Informacion actualizada correctamente")

def registrarProducto():
        id = int(input("Ingresa el ID: ")) 
        nombre = str(input("Ingresa nombre del producto: "))
        precio = float(input("Ingresa el precio del producto: "))
        clasificacion = str(input("Ingresa la clasificacion del producto: "))
        marca = str(input("Ingresa la marca del producto: "))
    
        objBebida = almacenBebidas(id, nombre,precio, clasificacion, marca)
        listaproductos.append(objBebida) 

def mostraralmacenBebidas(): 
        print("Lista de productos")
        for objBebida in listaproductos: 
            objBebida.entregarInformacion() 

"""def mostrar():
    print("Mostrar informacion")
    for objBebida in listaproductos: 
        objBebida.DarBaja()"""
    
def PrecioPromedio():
    print("Calcular precio promedio de bebidas")
    resultado = float(_precio)
    print("Precio promedio de bebida".format(resultado))
    
def BebidasMarca():
    print("Cantidad de bebidas de una marca")
    
def Clasificacion():
    print("cantidad por clasificacion")

    def salir():
    print("Salir del programa")
    exit()


def main():  
        while True:
            print("             MENU          ")
            print("1.- Dar de alta un producto")
            print("2.- Dar de baja un producto")
            print("3.- Mostrar productos")
            print("4.- Actualizar producto")
            print("5.- Salir")
         
            opcion = int(input("Opcion: "))

            if opcion == 1:
                DarAlta()
            elif opcion == 2:
                DarBaja()
            elif opcion == 3:
                mostraralmacenBebidas()
            elif opcion == 4:
                Actualizar()
            elif opcion == 5:
                salir()
        
if __name__ == '__main__':
    main()