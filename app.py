from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://RONEX_DB_owner:npg_6qaL8OTJFudn@ep-lingering-frost-a51pas0b-pooler.us-east-2.aws.neon.tech/RONEX_DB?sslmode=require&channel_binding=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "¡Backend Flask listo y funcionando con Neon PostgreSQL!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
