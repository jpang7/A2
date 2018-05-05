from flask import request, render_template, jsonify
from functools import wraps # for decorators
import app

# Models
from app.rent.models.all import *
#from app.rent.models.all import Housing

# DAO
from app.rent.dao import boards_dao

# Serializers
board_schema         = BoardSchema()

# Blueprint
from app.rent import rent
