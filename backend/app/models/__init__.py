from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .Files import Files
from .FileItems import FileItems