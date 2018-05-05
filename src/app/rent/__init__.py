from flask import Blueprint
from app import *

# Kanban Blueprint
rent = Blueprint('rent', __name__, url_prefix='/rent')

# Import all endpoints
from controllers.boards_controller import *
from controllers.housing_controller import *
