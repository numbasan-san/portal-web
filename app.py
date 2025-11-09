
# app.py
import random, logging
from flask import Flask, render_template, request, jsonify, url_for

# === CONFIGURACIÓN DE APP Y BD === #
app = Flask(__name__)

# === RUTAS PRINCIPALES === #
@app.route('/')
def index():
    data = {
        "title": "Integrantes",
        'integrantes': [
            {
                'nombre': 'Emanuel Solari Clase',
                'matricula': '23-0467',
                'img': '1.jpg',
            },
            {
                'nombre': 'Eddy Manuel Peña Ortega',
                'matricula': '23-1187',
                'img': '0.jpg',
            },
            {
                'nombre': 'Pedro Pablo De La Cruz Rojas',
                'matricula': '24-1424',
                'img': '2.png',
            }
        ]
    }
    return render_template("index.html", data=data)

@app.route('/definition')
def definition():
    return render_template("definition.html", data={"title": "Definición"})

@app.route('/structure')
def structure():
    return render_template("structure.html", data={"title": "Estructura"})

@app.route('/middle_end_code')
def middle_end_code():
    return render_template("middle_end_code.html", data={"title": "Código Medio y Final"})

@app.route('/phases')
def phases():
    return render_template("phases.html", data={"title": "Fases"})

@app.route('/compilers')
def compilers():
    return render_template("compilers.html", data={"title": "Compiladores"})

@app.route('/fonts')
def fonts():
    return render_template("fonts.html", data={"title": "Fuentes"})

# === MANEJO DE ERRORES === #
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', data={"title": "E R R O R : N O T - F O U N D"}), 404

# === EJECUCIÓN === #
if __name__ == '__main__':
    app.register_error_handler(404, not_found)
    app.run(debug=True, threaded=True)
