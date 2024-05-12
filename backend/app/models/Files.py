from datetime import datetime
from pytz import timezone
from sqlalchemy.inspection import inspect
from sqlalchemy.types import Integer, String, SmallInteger, DateTime
from sqlalchemy.schema import Column
from app.models import db

date = lambda : datetime.now(timezone('America/Sao_Paulo'))

class Files(db.Model):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, unique=True)
    filename = Column(String(100), nullable=False)    
    created_at = Column(DateTime, nullable=False, default=date)
    updated_at = Column(DateTime, default=date, onupdate=date)
    status = Column(SmallInteger, unique=False, default=1)
    
    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
