from flask import Flask
from flask_restful import Api
from resources.appointment import Appointments, Appointment
from resources.user import User, UserRegister, UserLogin
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbteste.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your-secret-key-change-this'  # Adicionar chave JWT
app.config['JWT_IDENTITY_CLAIM'] = 'sub'  # Permitir diferentes tipos de identity
api = Api(app)
jwt = JWTManager(app)

# Remover before_first_request - não é mais necessário
# O banco será criado automaticamente quando necessário

api.add_resource(Appointments, '/appointments')
api.add_resource(Appointment, '/appointments/<int:appointment_id>')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
  from sql_alchemy import db
  db.init_app(app)
  
  # Criar tabelas dentro do contexto da aplicação
  with app.app_context():
    db.create_all()
  
  app.run(debug=True)
    