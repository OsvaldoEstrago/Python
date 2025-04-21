from flask import Flask, render_template, redirect, url_for,request, flash, session

import webbrowser
from config import config
import globales
import funciones  as f


app = Flask(__name__)


@app.route('/')
def home():
    xAvance     = 'Se ingresan los datos de Identificación'
    xIdentidad  =  0
    return render_template('index.html',xAvance=xAvance)


@app.route('/login', methods=['GET','POST'])
def login():
    
    xDocumento      =  request.form['documento']
    xClave          =  request.form['Clave']   

    
    f.verificausuario(1)
    xIdentidad = 1
    parametros = {
    'xDocumento' :  12,
    'xAvance'    :  "Acceso Verificado",
    'xNombre'    :  "Usuario de Prueba", 
    'xIdentidad' :  1,
    'xTarea004'  :  1,
                 }  
  
    if  xIdentidad  !=  1:
        return  render_template('index.html',**parametros)
    else:
        return  render_template('menu.html',**parametros) 

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()