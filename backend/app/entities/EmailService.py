import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import app

class EmailService():
    
    def __init__(self):
        username = app.app.config['EMAIL_USERNAME']
        password = app.app.config['EMAIL_PASSWORD']
        address = app.app.config['EMAIL_ADDRESS']
        smtp_server = app.app.config['EMAIL_SMTP_SERVER']
        smtp_port = app.app.config['EMAIL_PORT']        
        
    
    def send (self, data):
        try:
            
            message = MIMEMultipart('alternative')
            message['subject'] = data['subject']
            message['from'] = self.address            
            message['to'] = data['sent_to']
            
            message.attach(MIMEText(data['body'], 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()            

            server.login(self.username, self.password)
            server.sendmail(self.username, data['sent_to'], data['body'].as_string())            
            server.quit()
            print("EMAIL ENCAMINHADO")
            
            return True
        except Exception as e:
            print(e)
            print("EMAIL NÃO ENCAMINHADO -> " + data['sent_to'])
            return False