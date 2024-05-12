import importlib
import os
from flask import Flask
from flask_cors import CORS
from app.models import db
from app.entities.CustomJSONEncoder import CustomJSONEncoder
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)    

    app.json_encoder = CustomJSONEncoder    
    
    environ = {        
        'prod': 'app.entities.Config.ProductionConfig'
    }    

    conf = environ.get(os.environ.get('FLASK_CONF', default='prod'))
    app.config.from_object(conf)
    db.init_app(app)
    
    CORS(app)
    Migrate(app=app, db=db, compare_type=True)   

    mod = importlib.import_module('.'.join(conf.split('.')[:-1]))
    env = getattr(mod, conf.split('.')[-1:][0])

    for module in env.MODULES:
        try:            
            package = importlib.import_module('app.views')            
            app.register_blueprint(
                getattr(package, module),
                url_prefix='/api/{}'.format(module)
            ) 
        except Exception as e:
            print(str(e))
    
    return app

app = create_app()
