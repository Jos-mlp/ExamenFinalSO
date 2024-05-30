from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    nombre = "Josue Manuel Maldonado Lepe"
    carnet = "1664220"
    url="Universidad Rafael Landivar"
    facultad="Facultad ingenieria"
    curso="Sistemas operativos"
    edad = 21  
    return render_template('index.html', nombre=nombre,carnet=carnet,url=url,
                           facultad=facultad,curso=curso, edad=edad)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
