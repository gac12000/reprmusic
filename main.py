from flask import Flask, render_template, request
import schedule
import threading
import time
import os

app = Flask(__name__)

# Lista en memoria RAM (se borra al reiniciar el Repl)
programacion = []

def ejecutar_musica(url):
    # En Replit no podemos abrir 'webbrowser' porque es un servidor remoto.
    # Imprimimos el log. Para que suene en TU PC, deberías tener la web abierta.
    print(f"--- [ALERTA] Toca reproducir: {url} ---")

def scheduler_loop():
    while True:
        schedule.run_pending()
        time.sleep(5)

@app.route('/')
def index():
    return render_template('index.html', espacios=range(8))

@app.route('/programar', methods=['POST'])
def programar():
    schedule.clear()
    conteo = 0
    for i in range(8):
        url = request.form.get(f'url_{i}')
        inicio = request.form.get(f'inicio_{i}')
        
        if url and inicio:
            schedule.every().day.at(inicio).do(ejecutar_musica, url)
            conteo += 1
            
    return f"<h1>Sincronizado: {conteo} canciones programadas.</h1><p>Revisa la consola de Replit.</p>"

if __name__ == '__main__':
    # Hilo para el reloj
    threading.Thread(target=scheduler_loop, daemon=True).start()
    # Replit necesita correr en 0.0.0.0
    app.run(host='0.0.0.0', port=8080)
