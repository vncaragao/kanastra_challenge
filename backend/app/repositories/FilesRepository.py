from app.models import db, Files, FileItems
from sqlalchemy import or_, func

class FilesRepository():
    def list():
        try:
            query = db.session.query(
                Files.filename,
                Files.updated_at,
                func.ifnull(func.count(FileItems.id), 0 ),
                Files.status
            ).outerjoin(
                FileItems
            ).group_by(
                Files.id
            ).all()
           
            result = []
            for row in query:
                result.append({
                    'filename': row[0],
                    'last_update': row[1].strftime('%d-%m-%Y %H:%M:%S'),
                    'items': row[2],
                    'status': 'Ativo' if row[3] == 1 else 'Finalizado'
                })
            
            status = 200
            if result == []:
                status = 404
           
            return {'result': result, 'status': status}
        except Exception as e:  
            print(e)          
            return {'msg': 'Error', 'status': 406}