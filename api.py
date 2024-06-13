from flask import Blueprint, request
from db import Content, db
from json import dumps

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/contents', methods = ['GET'])
def getAll():
    data = Content.query.all()
    return dumps({'contents': [{'id': content.id, 'detail': content.detail} for content in data]})

@api.route('/contents/<int:id>', methods=['GET'])
def get(id):
    content = Content.query.filter_by(id=id).first()
    return dumps({'id': content.id, 'detail': content.detail})

@api.route('/contents', methods=['POST'])
def add():
    json = request.get_json()
    entry = Content()
    entry.detail = json['detail']
    db.session.add(entry)
    db.session.commit()
    db.session.close()
    return 'Successfully added the content'

@api.route('/contents/<int:id>', methods=['PUT'])
def put(id):
    json = request.get_json()
    entry = Content.query.get(id)
    entry.detail = json['detail']
    db.session.merge(entry)
    db.session.commit()
    db.session.close()
    return 'Successfully put the content'

@api.route('/contents/<int:id>', methods=['DELETE'])
def delete(id):
    entry = Content.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    db.session.close()
    return 'Successfully deleted the content'
