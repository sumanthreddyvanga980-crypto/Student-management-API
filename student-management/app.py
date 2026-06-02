import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.abspath(os.path.dirname(__file__))
database_path = os.getenv('DATABASE_FILE')
if not database_path:
    if os.getenv('VERCEL'):
        database_path = os.path.join('/tmp', 'students.db')
    else:
        database_path = os.path.join(base_dir, 'students.db')

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from routes import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))