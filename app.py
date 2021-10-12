import os
from flask import Flask, request
from flask.templating import render_template
from forms import FormLogin
from usuariospre import lista_usuarios
from forms import FormRegistro

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/registro/', methods=('GET', 'POST'))
def registro():
    mensaje = ""

    if request.method == "GET": 
        formulario = FormRegistro()
        return render_template('registro.html')
    elif request.method== "POST":
        formulario = FormRegistro(request.form)
        if formulario.validate_on_submit():
            if validar_usuario(formulario.usuario.data):
                if (formulario.password.data != formulario.repassword.data):
                      mensaje += "Las contraseñas no coinciden."   
            else:
                mensaje += "El usuario no es válido o ya fue registrado"
        else:
            mensaje += "Todos los datos son requeridos."
        
        if not mensaje:
            mensaje = "Su cuenta ha sido registrada, puede iniciar sesión."
            return render_template('registro.html', errores = mensaje)
        else:
            render_template('registro.html',form=FormRegistro, errores = mensaje)


@app.route('/login/', methods=["GET", "POST"])
def login():
    mensaje = ""

    if request.method == "GET":
        formulario = FormLogin()
        return render_template('login.html', titulo='Iniciar Sesión', form=formulario)
    else:
        formulario = FormLogin(request.form)
        if formulario.validate_on_submit():
            if validar_login(formulario.usuario.data,formulario.password.data):
                mensaje = "El usuario {0} inició sesión".format(formulario.usuario.data)
                return render_template('Index.html',mensaje=mensaje)
            else:
                mensaje = "Los datos ingresados NO son válidos."
               
        mensaje += "Todos los datos son requeridos"
        return render_template('Login.html',form=FormLogin(), errores=mensaje)
        

def validar_login(usuario,password):
    for i in range(len(lista_usuarios)):
        if lista_usuarios[i]["usuario"] == usuario:
            if lista_usuarios[i]["password"] == password:
                return True

    return False


def validar_usuario(usuario):
    for i in range(len(lista_usuarios)):
        if lista_usuarios[i]["usuario"] == usuario:
            if lista_usuarios[i]["password"] == None:
                return True

    return False  
  
    