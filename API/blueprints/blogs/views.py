from flask import Blueprint , request
from flask.json import jsonify
from models.blog import Blog
from models.user import User
from flask_jwt_extended import jwt_required

blogs_api_blueprint = Blueprint('blogs_api',
                             __name__,
                             template_folder='templates')

### SHOW ALL BLOG 
@blogs_api_blueprint.route("/",methods=['GET'])
def index():
    blog_query = Blog.select()
    blog_list = []

    for b in blog_query:
        blog_list.append(b.as_dict())

    result = jsonify({
        'data':blog_list
    })

    return result




### CREATE BLOG
@blogs_api_blueprint.route('/new',methods=['POST'])
@jwt_required
def create():
    data = request.form

    new_blog = Blog.create(
        parent_user = data['user_id'],
        desc = data['desc'],
        title = data['title']
    )

    new_blog.save()

    result = jsonify({
        'status':True,
        'data' : new_blog.as_dict()
    })

    return result

### ONE BLOG
@blogs_api_blueprint.route('/<id>',methods=["GET"])
def show(id):
    blog = Blog.get_or_none(Blog.id==id)
    blog_found = blog!=None
    result = jsonify({
        'status':blog_found,
        'data':blog.as_dict()
    })

    return result