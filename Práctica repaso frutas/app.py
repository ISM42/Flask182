from flask import Flask,render_template,request,redirect,url_for, flash 
from flask_mysqldb import MySQL

app= Flask(__name__) 
app.config['MYSQL_HOST']= "localhost"  
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""
app.config['MYSQL_DB']= "db_fruteria"

app.secret_key='mysecretkey'
mysql= MySQL(app) 

@app.route('/')  
def index():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from tbfrutas')
   
    consulta=curSelect.fetchall() 
   

    return render_template('index.html',listFrutas=consulta)

@app.route('/guardar',methods=['POST'])
def guardar(): 
    if request.method == 'POST':
        _fruta=request.form['txtFruta']
        _temporada=request.form['txtTemporada']
        _precio=request.form['txtPrecio']
        _stock=request.form['txtStock']
      
        curGuardar=mysql.connection.cursor()
        curGuardar.execute('insert into tbfrutas(fruta,temporada,precio,stock) values(%s,%s,%s,%s)',(_fruta, _temporada, _precio, _stock))
        mysql.connection.commit()
        
    flash('Producto agregado correctamente')
    return redirect(url_for('index'))
     
@app.route('/inventario') 
def inventario():
    cur=mysql.connection.cursor()
    cur.execute('select * from tbfrutas')
    consulId=cur.fetchall() 
    return render_template('inventario.html',listFrutas=consulId)

@app.route('/editar/<id>') 
def editar(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from tbfrutas where id = %s',(id,))
    consulId=curEditar.fetchone() 
    return render_template('actualizar.html',fruta=consulId)

@app.route('/actualizar/<id>',methods=['POST']) 
def actualizar(id): 
   if request.method == 'POST':
        _fruta=request.form['txtFruta']
        _temporada=request.form['txtTemporada']
        _precio=request.form['txtPrecio']
        _stock=request.form['txtStock']

        curAct=mysql.connection.cursor()
        curAct.execute('update tbfrutas set fruta=%s, temporada=%s, precio=%s, stock =%s where id = %s', (_fruta,_temporada, _precio, _stock ,id))
        mysql.connection.commit()

        flash('Producto actualizado en la base de datos correctamente')
        return redirect(url_for('index'))
     
@app.route('/eliminarfruta/<id>') 
def eliminarfruta(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from tbfrutas where id = %s',(id,))
    consulId=curEditar.fetchone() 
    return render_template('eliminarfruta.html',fruta=consulId)

@app.route('/eliminar/<id>', methods=['POST'])
def eliminar(id):
    if request.method == 'POST':
        _fruta=request.form['txtFruta']
        _temporada=request.form['txtTemporada']
        _precio=request.form['txtPrecio']
        _stock=request.form['txtStock']
        
        curEliminar=mysql.connection.cursor()
        curEliminar.execute('delete from tbfrutas  where id = %s', (id))
        mysql.connection.commit()

        flash('Producto eliminado en la base de datos correctamente')
    return redirect(url_for('index'))   

@app.route('/buscador') 
def buscador():
    #cur=mysql.connection.cursor()
   # cur.execute('select * from tbfrutas')
    #consulId=cur.fetchall() 
    return render_template('consulta_fruta.html')

@app.route('/consultafruta', methods=['POST','GET']) 
def consultafruta():
    if request.method == 'POST':
        _fruta=request.form['txtFruta']
          
        curbuscar=mysql.connection.cursor()
        curbuscar.execute('select * from tbfrutas where fruta like %s',(_fruta,))
   
        resultadoBusqueda=curbuscar.fetchone() 
  #cur.close()
    return render_template('consulta_fruta.html',_fruta='_txtFruta' )
    return redirect(url_for('index'))

@app.route('/resultadobusqueda') 
def resultadobusqueda():
    curbuscar=mysql.connection.cursor()
    curbuscar.execute('select * from tbfrutas where fruta like %s',(_fruta,)) #REVISAR PARÁMETRO
    resultadoBusqueda=curbuscar.fetchone() 

    return render_template('consulta_fruta.html',_fruta='_txtFruta')

if __name__== '__main__':
    app.run(port=5000,debug=True)  
