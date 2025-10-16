from flask import Flask
from flask_restful import Api
from resources.appointment import Appointments, Appointment

app = Flask(__name__)
api = Api(app)

api.add_resource(Appointments, '/appointments')
api.add_resource(Appointment, '/appointments/<int:appointment_id>')

if __name__ == '__main__':
  app.run(debug=True)
    