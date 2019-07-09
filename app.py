import sqlite3
from flask import Flask
from flask import render_template #convierte python en html y viceversa
from flask import request
import os #ayuda a mejorar la comunicacion entre los archivos de la aplicacion
from flask_sqlalchemy import SQLAlchemy #para que entienda que se esta trabajando con SQL

app = Flask(__name__)

direccion = "Sqlite:///" + os.path.abspath(os.getcwd()) + "database.db"
app.config ["SQLALCHEMY_DATABASE_URL"] = direccion #comunicacion con la bd

#---------------------------------------------------------------------------------------------
#Funciones
#---------------------------------------------------------------------------------------------
def get_db():

   #Se conecta a la base de datos, agrega una fila

   db = getattr(g, '_database', None)

   if db is None:
      db = g._database = sqlite3.connect(direccion)
      db.row_factory = sqlite3.Row  
   
   return db
#---------------------------------------------------------------------------------------------
#@app.route('/')
@app.route('/agregar', methods = ['GET', 'POST'])
#def introduccion():
   #return  render_template("index.html")

def agregar():
   #revisamos si la tabla comida en el campo Name se encuentra vacia
   if request.method == "GET":
      return render_template("paginaagregar.html", comida= Name)
   #INSERTAR
   if request.method == "POST":
      comida = request.formato_dict()
      values = [comida['fecha'],comida['lugar'],comida['tipo'],comida['monto']] #revisa que existan los campos en formulario
      change_db("INSERT INTO comida (fecha, lugar, tipo, monto) VALUES(?,?,?,?)", values)
      return render_template("exito.html")

#return redirect (url_for ("agregar")) #Busca la direccion del archivo
   

if  __name__ == '__main__':
   app.run(debug=True)

