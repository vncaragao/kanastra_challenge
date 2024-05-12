from flask.json import jsonify
from flask.views import MethodView
from flask_restful import reqparse
from app.repositories.FilesRepository import FilesRepository
from werkzeug.datastructures import FileStorage
from io import StringIO
from csv import DictReader
from app.services.ProcessFile import ProcessFile
from app.repositories.BaseResource import BaseResource
from app.models import Files
from werkzeug.utils import secure_filename

class FilesController(MethodView):    
    
    def get(self):
        
        result = FilesRepository.list()
        
        return jsonify(result['result']), result['status']
    
    
    def post(self):
        parser = reqparse.RequestParser()                     
        parser.add_argument('file', type=FileStorage,
                                location='files', required=True)            
        data = parser.parse_args()

        mailingData = []
        
        if data['file'].content_type == 'text/csv':
            stream = StringIO(
            data['file'].stream.read().decode('UTF-8'), newline=None)
            csv_input = DictReader(stream, delimiter=',')            
            csv_input.fieldnames[0] = csv_input.fieldnames[0].replace('\ufeff', '') 
            mailingData = list(csv_input)
        else:
            return jsonify({'msg': 'Invalid File'}), 406
        
        newFile = BaseResource(Files).postData({ "filename": secure_filename(data['file'].filename)})
        
        ProcessFile(mailingData, newFile['result']['id'])
        
        return jsonify({'msg': 'File received'}), 200