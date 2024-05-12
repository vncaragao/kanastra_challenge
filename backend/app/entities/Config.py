import os

class BaseConfig(object):
    DEBUG  = False
    TESTING = False
    SECRET_KEY = os.urandom(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MODULES = [
        'files'
    ]
    
class ProductionConfig(BaseConfig):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite'    
    MODULES = BaseConfig.MODULES
    EMAIL_USERNAME = ""
    EMAIL_PASSWORD = ""
    EMAIL_ADDRESS = ""
    EMAIL_SMTP_SERVER = ""
    EMAIL_PORT = ""