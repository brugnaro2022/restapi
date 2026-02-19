from sql_alchemy import db

class AppointmentModel(db.Model):
  __tablename__ = 'appointments'

  appointment_id = db.Column(db.String, primary_key=True)
  name = db.Column(db.String(80))
  description = db.Column(db.String(200))
  
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

  @classmethod
  def find_appointment(cls, appointment_id):
    appointment = cls.query.filter_by(appointment_id = appointment_id).first() # SELECT * FROM appointments WHERE appointment_id = appointment_id
    if appointment:
      return appointment
    return None


  def save_appointment(self):
    db.session.add(self)
    db.session.commit()

  def update_appointment(self, name, description):
    self.name = name
    self.description = description

  def delete_appointment(self):
    db.session.delete(self)
    db.session.commit()