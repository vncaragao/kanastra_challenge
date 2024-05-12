from datetime import datetime
from pytz import timezone
from sqlalchemy.inspection import inspect
from sqlalchemy.types import Integer, String, SmallInteger, DateTime, Float, Date
from sqlalchemy.schema import Column, ForeignKey
from app.models import db

date = lambda : datetime.now(timezone('America/Sao_Paulo'))

class FileItems(db.Model):
    __tablename__ = "file_items"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(255), nullable=False)
    governmentId = Column(Integer, nullable=False)    
    email = Column(String(100), nullable=False)
    debtAmount = Column(Float, nullable=False, default =0.0)
    debtDueDate = Column(Date, nullable=False)
    debtId = Column(String(50), nullable=False)
    date_event = Column(DateTime, nullable=False, default=date)    
    processed = Column(SmallInteger, nullable=False, default=1) 
    file_id = Column(Integer, ForeignKey('files.id'), nullable=False)
    
    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
