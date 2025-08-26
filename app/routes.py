from app import app

@app.route('/')
def index():
    return "¡Backend Flask modular listo y funcionando con Neon PostgreSQL!"
