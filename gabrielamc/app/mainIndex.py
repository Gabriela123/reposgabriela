'''
Created on 19/1/2015

@author: PC27
'''


from app import app
from flask import render_template, request, redirect, url_for
from ec.edu.itsae.dao import PersonaDAO




@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login")
def login():
    usuario=request.args.get('username')
    clave=request.args.get('password')
    report=PersonaDAO.PersonaDAO().validarUsuario(usuario, clave)
    if len(report)==1:
        return redirect (url_for("main"))
    else :
        return redirect (url_for("index"))
    
    
@app.route("/main")
def main():
    return render_template("main.html")    
    