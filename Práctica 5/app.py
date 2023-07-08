#El app.py va a ser donde se hacen todas las configuraciones para el servidor de las peticiones que se harán a través del navegador
#el render template es una librería que nos permite mostrar la vista a través de la ruta especificada
#request es una librería para solicitudes
#redirect y url_for nos sirve para redireccionar a nuestro formulario terminado de llenar una vez
from flask import Flask,render_template,request,redirect,url_for, flash #importación de la librería
from flask_mysqldb import MySQL

app= Flask(__name__) #se declara el app y se inicializa el servidor Flask
app.config['MYSQL_HOST']= "localhost" #aquí tmb se hacen las configuraciones a la conexión al servidor de la BD
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""
app.config['MYSQL_DB']= "dbflask"

app.secret_key='mysecretkey'
mysql= MySQL(app) 
#declaración de rutas

#ruta index o ruta principal http://localhost:5000 o 127.0.0.1 en lugar de localhost
#la ruta se compone de nombre y la función que va ejecutar
@app.route('/') ##declarar la ruta y el nombre. La diagonal es por default. Es la primera ruta que el servidor va a buscar
def index():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from albums')
    #creamos la variable consulta para crear la lista que se va a desplegar en vista
    consulta=curSelect.fetchall() #fetchall para jalar la lista completa de registros
    #print(consulta)

    return render_template('index.html',listAlbums=consulta)
#cada ruta lleva su ruta y su función.
#con el método, la ruta va a atrapar la información por método POST, las rutas que no declaren el método usarán GET de forma predeterminada.
@app.route('/guardar',methods=['POST']) ##Una segunda ruta o más ya pueden tener otros nombres.
def guardar(): 
    if request.method == 'POST':
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
        #print(titulo,artista,anio)
        CS=mysql.connection.cursor()
        CS.execute('insert into albums(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
        mysql.connection.commit()
        
    flash('Album agregado correctamente')
    return redirect(url_for('index'))
     
#ruta para enviar a la vista "editarAlbum y que se muestre el registro a modificar"     
@app.route('/editar/<id>') 
def editar(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from albums where id = %s',(id,))
    consulId=curEditar.fetchone() #fetchone porque solo vamos a jalar un solo registro
    return render_template('editarAlbum.html',album=consulId)

#ruta que realiza el query de actualización en la BD y redirecciona al index con msj de validación
@app.route('/actualizar/<id>',methods=['POST']) 
def actualizar(id): 
   if request.method == 'POST':
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']

        curAct=mysql.connection.cursor()
        curAct.execute('update albums set titulo=%s, artista=%s, anio=%s where id = %s', (Vtitulo, Vartista, Vanio,id))
        mysql.connection.commit()

        flash('Album actualizado en la base de datos correctamente')
        return redirect(url_for('index'))
   
@app.route('/eliminaralbum/<id>') 
def eliminaralbum(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from albums where id = %s',(id,))
    consulId=curEditar.fetchone() #fetchone porque solo vamos a jalar un solo registro
    return render_template('eliminaralbum.html',album=consulId)
 


@app.route('/eliminar/<id>',methods=['POST']) 
def eliminar(id):
    if request.method=='POST':
      curEliminar=mysql.connection.cursor()
      curEliminar.execute('delete from albums where id = %s',(id,))
      mysql.connection.commit()
    #consulId=curEliminar.fetchone() #fetchone porque solo vamos a jalar un solo registro
    
    flash('Album eliminado correctamente de la BD')
    return redirect(url_for('index'))



#Líneas que ejectuan el servidor
if __name__== '__main__':
    app.run(port=5000,debug=True) #usar puertos desocupados como entre el 5000 y el 8000. No usar 3306 o 3308
    #el debug me sirve para que ya no me envíe errores por el debug en OFF