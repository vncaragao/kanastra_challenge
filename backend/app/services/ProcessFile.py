
from threading import Thread
from app.repositories.BaseResource import BaseResource
from app.models import FileItems, Files
from datetime import datetime
from app.entities.EmailService import EmailService

def ProcessFile(mailingData, file_id):
    def run():
        from app import app
        with app.app_context():
            for row in mailingData:
                row['file_id'] = file_id
                row['debtDueDate'] = datetime.strptime(row['debtDueDate'], "%Y-%m-%d")
                BaseResource(FileItems).postData(row)
                
                email ={
                    "subject": "Seu boleto chegou!",
                    "sent_to": row['email'],
                    "body": row['debtId']
                }
                EmailService().send(email)
            
            BaseResource(Files).putData({"id": file_id},{"status": 0})
            return
    
    Thread(target=run).start()
    
    return