from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/contents', methods = ['POST'])
def get_contents():
    return 'dekita'