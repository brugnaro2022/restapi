from flask_restful import Resource, reqparse
from models.appointment import AppointmentModel

appointments = [
  {
    'appointment_id': 1,
    'name': 'Primeiro',
    'description': 'Descrição do primeiro Agendamento'
  },
  {
    'appointment_id': 2,
    'name': 'Segundo',
    'description': 'Descrição do segundo Agendamento'
  },
  {
    'appointment_id':3,
    'name': 'Terceiro',
    'description': 'Descrição do terceiro Agendamento'
  },
]

class Appointments(Resource):
  def get(self):
    return {'appointments': appointments}
  
class Appointment(Resource):
  args = reqparse.RequestParser()
  args.add_argument('name')
  args.add_argument('description')
  
  def find_appointment(appointment_id):
    for appointment in appointments:
      if appointment['appointment_id'] == appointment_id:
        return appointment
    return None
  
  def get(self, appointment_id):
    appointment = Appointment.find_appointment(appointment_id)
    if appointment:
      return appointment
    return {'message': 'Appointment not found.'}, 404
  
  def post(self, appointment_id):
    data = Appointment.args.parse_args()
    appointment_object = AppointmentModel(appointment_id, **data)
    new_appointment = appointment_object.json()
    appointments.append(new_appointment)
    return new_appointment, 201
  
  def put(self, appointment_id):
    data = Appointment.args.parse_args()
    appointment_object = AppointmentModel(appointment_id, **data)
    new_appointment = appointment_object.json()
    appointment = Appointment.find_appointment(appointment_id)
    if appointment:
      appointment.update(new_appointment)
      return new_appointment, 200
    appointments.append(new_appointment)
    return new_appointment, 201 # Created
      
  def delete(self, appointment_id):
    global appointments
    appointments = [appointment for appointment in appointments if appointment['appointment_id'] != appointment_id]
    return {'message': 'Appointment deleted.'}