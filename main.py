from flask import Flask, render_template, request
import schedule
import threading
import time
import os

app = Flask(__name__)

# Memoria volátil
biblioteca = []

def reproducir_logica(url):
    # Esto imprime en la consola de Replit cuando la hora coincide
    print(f"\n--- [EJECUTANDO] ---")
    print(f"Hora: {time.strftime('%H:%M:%S')}")
    print(f"Abriendo: {url}")
    print(f"--------------------\n")
    
    # Nota: En Replit, para que "suene", el servidor debe tener 
    # salida de audio configurada, lo cual es limitado.
    # Esta función simula la activación del trigger.

def stop_logica():
    print(f"--- [DETENIDO] Hora de cierre alcanzada ---")

def worker_reloj():
    while True:
        schedule.run_pending()
        time.sleep(1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/programar', methods=['POST'])
def programar():
    schedule.clear()
    for i in range(8):
        url = request.form.get(f'url_{i}')
        inicio = request.form.get(f'inicio_{i}')
        fin = request.form.get(f'fin_{i}')
        
        if url and inicio:
            schedule.every().day.at(inicio).do(reproducir_logica, url)
            if fin:
                schedule.every().day.at(fin).do(stop_logica)
                
    return "<h1>✅ Sistema Programado</h1><p>Revisa la consola de Replit para ver la ejecución.</p>"

if __name__ == "__main__":
    # Iniciar el reloj en segundo plano
    threading.Thread(target=worker_reloj, daemon=True).start()
    # Ejecutar servidor web en el puerto de Replit
    app.run(host='0.0.0.0', port=8080)
