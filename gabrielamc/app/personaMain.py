'''
Created on 19/1/2015

@author: PC27
'''
from app import app
from ec.edu.itsae.dao import PersonaDAO
from flask import render_template, request, redirect, url_for


@app.route("/mainPersonaX")
def mainPersona():
    objR=PersonaDAO.PersonaDAO().reportarPersona()
    return render_template("prueba.html", data=objR)



@app.route("/addPersona", methods=['POST','GET'])
def addPersona():
    
    nombre=request.form.get('nombre', type=str)
    print nombre
    apaterno=request.form.get('apaterno', type=str)
    amaterno=request.form.get('amaterno', type=str)
    cedula=request.form.get('cedula', type=str)
    fnacimiento=request.form.get('fnacimiento', type=str)
    sexo=request.form.get('sexo', type=str)
    direccion=request.form.get('direccion', type=str)
    celular=request.form.get('celular', type=str)
    estado=request.form.get('estado', type=int)
    
    
    PersonaDAO.PersonaDAO() .insertarPersona(nombre,apaterno,amaterno,cedula,fnacimiento,sexo,direccion,celular,estado)
    return redirect(url_for('mainPersona'))
        
        
@app.route("/buscarauto")
def buscarPersonaAuto():
    nombre=(request.args.get('term'))
    objR=PersonaDAO.PersonaDAO().buscarPersonaNombre(nombre)

    return objR    
        
        
@app.route("/buscardato")
def buscarPersonaDato():
    nombre=str(request.args.get('bnombre'))
    objR=PersonaDAO.PersonaDAO().buscarPersonaDato(nombre)
    return render_template("prueba.html", data=objR)    
    
    return objR