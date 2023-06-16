#El app.py va a ser donde se hacen todas las configuraciones para el servidor de las peticiones que se harán a través del navegador

from flask import Flask #importación de la librería

app= Flask(__name__) #se declara el app y se inicializa el servidor Flask
app.config['MYSQL_HOST']= "localhost" #aquí tmb se hacen las configuraciones a la conexión al servidor de la BD
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""
app.config['MYSQL_DB']= "bdflask"

#declaración de rutas

#ruta index o ruta principal http://localhost:5000 o 127.0.0.1 en lugar de localhost
#la ruta se compone de nombre y la función que va ejecutar
@app.route('/') ##declarar la ruta y el nombre. La diagonal es por default. Es la primera ruta que el servidor va a buscar
def index():
    return "Hola Mundo"
#cada ruta lleva su ruta y su función.
@app.route('/guardar') ##Una segunda ruta o más ya pueden tener otros nombres.
def guardar():
    return "Se guardo el album en la BD"

@app.route('/eliminar') 
def eliminar():
    return "Se elimino el album de la BD"    

#Líneas que ejectuan el servidor
if __name__== '__main__':
    app.run(port=5000,debug=True) #usar puertos desocupados como entre el 5000 y el 8000. No usar 3306 o 3308
    #el debug me sirve para que ya no me envíe errores por el debug en OFF