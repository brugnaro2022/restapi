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
    return {'appointments': [appointment.json() for appointment in AppointmentModel.query.all()]}
  
class Appointment(Resource):
  args = reqparse.RequestParser()
  args.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank")
  args.add_argument('description', type=str, required=True, help="The field 'description' cannot be left blank")
  
  def get(self, appointment_id):
    appointment = AppointmentModel.find_appointment(appointment_id)
    if appointment:
      return appointment.json()
    return {'message': 'Appointment not found.'}, 404
  
  def post(self, appointment_id):
    if AppointmentModel.find_appointment(appointment_id):
      return {"message": "Appointment id '{}' already exists.".format(appointment_id)}, 400 # Bad Request
    
    data = Appointment.args.parse_args()
    appointment = AppointmentModel(appointment_id, **data)
    
    try:
      appointment.save_appointment()
    except:
      return { "message": "An internal error occurred trying to save appointment." }, 500 # Internal Server Error

    return appointment.json()
    
  def put(self, appointment_id):
    data = Appointment.args.parse_args()
    appointment_found = AppointmentModel.find_appointment(appointment_id)
    if appointment_found:
      appointment_found.update_appointment(**data)
      appointment_found.save_appointment()
      return appointment_found.json(), 200
    appointment = AppointmentModel(appointment_id, **data)

    try:
      appointment.save_appointment()
    except:
      return { "message": "An internal error occurred trying to save appointment." }, 500 # Internal Server Error

    return appointment.json(), 201
      
  def delete(self, appointment_id):
    appointment = AppointmentModel.find_appointment(appointment_id)
    if appointment:
      try:
        appointment.delete_appointment()
      except:
        return { "message": "An error occurred trying to delete appointment." }, 500 # Internal Server Error
      
      return {'message': 'Appointment deleted.'}
    return {'message': 'Appointment not found.'}, 404
    