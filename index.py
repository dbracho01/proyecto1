from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route('/')
def principal():
    # return "Bienvenido o bienvenida a mi sitio web con python!"
    return "DAVID BRACHO"

@app.route('/contacto')
def contacto():
    return "Esta es la página de contacto"
"""


@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/lenguajes')
def mostrarLenguajes():
    misLenguajes = ("Mosfet", "Resistencia", "Diodos", "Esp 32",
                    "FPGA")
    return render_template('lenguajes.html', lenguajes=misLenguajes)


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

#en la linea 35 se cambia el puerto y el debug para reiniciar el servidor automatico
if __name__ == '__main__':
    app.run(debug=True, port=5300)
