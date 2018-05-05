from app.constants import *
from . import *

@rent.route('/boards', methods=['GET', 'POST', 'DELETE'])
def boards_crud():
  return jsonify("Hello World!")
