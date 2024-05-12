from flask import Blueprint

files = Blueprint('files', __name__)

from .controllers import *

files.add_url_rule('/', view_func=FilesController.as_view('FilesController'), methods=['GET','POST'])