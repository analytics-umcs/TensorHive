from tensorhive.models.User import User
from tensorhive.models.Role import Role
from connexion import NoContent
from flask_jwt_extended import create_access_token, create_refresh_token

class CreateUserController():
    # TODO Add more user parameters

    @staticmethod
    def create(user):
        if User.find_by_username(user['username']):
            # Duplicated resource
            return NoContent, 409

        new_user = User(username=user['username'], password=user['password'])

        if new_user.save_to_db():
            new_role = Role(name='user', user_id=new_user.id)
            if new_role.save_to_db():
                return {
                    'msg': 'User {} successfully created'.format(user['username']), **new_user.as_dict
                }, 201
            else:
                return NoContent, 500

        else:
            return NoContent, 500

        