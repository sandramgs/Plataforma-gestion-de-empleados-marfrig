from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField, TextAreaField
from wtforms import validators

class FormLogin(FlaskForm):
    usuario = StringField('Usuario',validators=[validators.required(),validators.length(max=20),validators.DataRequired(message="No deje vacio este campo, esciba el usuario")])
    password = StringField('Contraseña',validators=[validators.required(),validators.length(max=50),validators.DataRequired(message="No deje vacio este campo, esciba la contraseña")])
    ingresar = SubmitField("Ingresar")

class FormRegistro(FlaskForm):
    usuario = StringField('Usuario',validators=[validators.required(),validators.length(max=20),validators.DataRequired(message="No deje vacio este campo, esciba el usuario")])
    password = StringField('Contraseña',validators=[validators.required(),validators.length(max=50),validators.DataRequired(message="No deje vacio este campo, esciba la contraseña")])
    repassword = StringField("Confirmar Contraseña", validators=[validators.required(),validators.length(max=50),validators.DataRequired(message="No deje vacio este campo, re escriba la contraseña")])
    enviar = SubmitField("Enviar Mensaje")
