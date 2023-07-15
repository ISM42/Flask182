from flask import Flask,render_template,request,redirect,url_for, flash 
from flask_mysqldb import MySQL

app= Flask(__name__) 
app.config['MYSQL_HOST']= "localhost" 
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""
app.config['MYSQL_DB']= "db_floreria"

app.secret_key='mysecretkey'
mysql= MySQL(app) 

@app.route('/') 
def index():
    index=mysql.connection.cursor()
    index.execute('select * from tbflores')
    consulta=index.fetchall() 
   
    return render_template('index.html',listaFlores=consulta)

@app.route('/guardar',methods=['POST']) 
def guardar(): 
    if request.method == 'POST':
       _nombre=request.form['txtNombre']
       _cantidad=request.form['txtCantidad']
       _precio=request.form['txtPrecio']
        
       guardar=mysql.connection.cursor()
       guardar.execute('insert into tbflores(nombre,cantidad,precio) values(%s,%s,%s)',(_nombre,_cantidad,_precio))
       mysql.connection.commit()
        
    flash('Producto agregado correctamente')
    return redirect(url_for('index'))


@app.route('/vinventario') 
def inventario():
    inv=mysql.connection.cursor()
    inv.execute('select * from tbflores')
    mysql.connection.commit()

    consulta_inv=inv.fetchall() 
    return render_template('consulta.html',listaFlor=consulta_inv)

      
@app.route('/vactualizar/<id>') 
def editar(id):
    editar=mysql.connection.cursor()
    editar.execute('select * from tbflores where id = %s',(id,))
    consulta=editar.fetchone() 
    return render_template('actualizar_producto.html',flores=consulta)


@app.route('/actualizar/<id>',methods=['POST']) 
def actualizar(id): 
   if request.method == 'POST':
       _nombre=request.form['txtNombre']
       _cantidad=request.form['txtCantidad']
       _precio=request.form['txtPrecio']

       curAct=mysql.connection.cursor()
       curAct.execute('update tbflores set nombre=%s, cantidad=%s, precio=%s where id = %s', (_nombre,_cantidad,_precio,id))
       mysql.connection.commit()

       flash('Producto actualizado en la base de datos correctamente')
       return redirect(url_for('index'))
   
@app.route('/veliminar/<id>') 
def eliminarProducto(id):
    eliminar=mysql.connection.cursor()
    eliminar.execute('select * from tbflores where id = %s',(id,))
    consulta=eliminar.fetchone()
 
    return render_template('eliminar_producto.html',flores=consulta)


@app.route('/eliminar/<id>',methods=['POST']) 
def eliminar(id):
    if request.method=='POST':
      eliminar=mysql.connection.cursor()
      eliminar.execute('delete from tbflores where id = %s',(id,))
      mysql.connection.commit()

    
    flash('Producto eliminado correctamente de la BD')
    return redirect(url_for('index'))



if __name__== '__main__':
    app.run(port=5000,debug=True) 
    
