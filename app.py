from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

# Definir la ruta principal de la aplicación
@app.route('/')
def index():
    # Realizar una solicitud a la API para obtener los datos
    url = "https://rickandmortyapi.com/api/character/2"  # Reemplaza con la URL real de tu API
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = json.loads(response.text)
        except json.JSONDecodeError as e:
            print("Error al analizar JSON:", e)
            data = []
    else:
        print("Error en la solicitud a la API:", response.status_code)
        data = []

    # Renderizar la plantilla HTML y pasar los datos
    return render_template('template.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
