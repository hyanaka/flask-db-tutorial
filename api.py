from flask import Blueprint
from db import Content
from json import dumps

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/contents', methods = ['GET'])
def get_contents():
    data = Content.query.all()
    return dumps({'contents': [{'id': content.id, 'detail': content.detail} for content in data]})