from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token
import hmac

# Substituição para safe_str_cmp removido do Werkzeug 2.2+
def safe_str_cmp(a, b):
    return hmac.compare_digest(str(a), str(b))

params = reqparse.RequestParser()
params.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
params.add_argument('password', type=str, required=True, help="The field 'password' cannot be left blank")

class User(Resource):
  # /users/{user_id}
  def get(self, user_id):
    user = UserModel.find_user(user_id)
    if user:
      return user.json()
    return {'message': 'User not found.'}, 404
      
  def delete(self, user_id):
    user = UserModel.find_user(user_id)
    if user:
      try:
        user.delete_user()
      except:
        return { "message": "An error occurred trying to delete user." }, 500 # Internal Server Error
      return {'message': 'User deleted.'}
    return {'message': 'User not found.'}, 404  

class UserRegister(Resource):
  # /register
  def post(self):
    data = params.parse_args()

    if UserModel.find_by_login(data['login']):
      return {"message": "The login '{}' already exists.".format(data['login'])}
    
    user = UserModel(**data)
    user.save_user()
    return {"message": "User created successfully!"}, 201 # Created

class UserLogin(Resource):

  @classmethod
  def post(cls):
    data = params.parse_args()

    user = UserModel.find_by_login(data['login'])

    if user and safe_str_cmp(user.password, data['password']):
      access_token = create_access_token(identity=user.user_id)
      return {'access_token': access_token}, 200
    return {'message': 'The username or password is incorrect.'}, 401 # Unauthorized


