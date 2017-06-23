
from ark.db import Database
from sqlalchemy import Column, Integer
from sqlalchemy.dialects import postgresql
db = Database('postgresql://oceanuse:851JqIaLicRwkGs@10.30.183.102:5432/ocean')

class Test(db.Model):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
query = db.session.query(Test).limit(10).offset(-1)
print query.all()
