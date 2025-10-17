class AppointmentModel:
  def __init__(self, appointment_id, name, description):
    self.appointment_id = appointment_id
    self.name = name
    self.description = description
    
  def json(self):
    return {
      'appointment_id': self.appointment_id,
      'name': self.name,
      'description': self.description
    }