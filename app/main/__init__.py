from flask import Blueprint

mail=Blueprint('main', __name__)

from . import views, errors 
