from flask import Flask
from flask_restful import Api
from resources.appointment import Appointments, Appointment
from resources.user import User, UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbteste.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_request
def create_db():
  db.create_all()

api.add_resource(Appointments, '/appointments')
api.add_resource(Appointment, '/appointments/<int:appointment_id>')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
  from sql_alchemy import db
  db.init_app(app)
  app.run(debug=True)
    