from flask import Blueprint , request
from models.user import User
from flask.json import jsonify
from werkzeug.security import generate_password_hash , check_password_hash

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('/', methods=['GET'])
def index():
    selected_users = User.select()
    result = jsonify({
        'data' : [u.as_dict() for u in selected_users]
    })
    return result

### CREATE NEW USER
@users_api_blueprint.route('/', methods=['POST'])
def create():
    data = request.form
    hashed_password = generate_password_hash(data['password'])

    new_user = User(
        email = data['email'],
        username = data['username'],
        password = hashed_password
    )

    new_user.save()

    successfully_created = (User.get_or_none( User.username ==  new_user.username ) != None)

    resutl = jsonify({
        'status' : successfully_created,
        'data': new_user.as_dict()
    })

    return result