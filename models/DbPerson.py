from config import db

class DbPerson(db.Model):
    __tablename__='employee'
    eno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),index=False,unique=False,nullable=False)
    city=db.Column(db.String(30),index=False,unique=False,nullable=False)
    designation=db.Column(db.String(30),index=False,unique=False,nullable=False)
    basic=db.Column(db.Integer,index=False,unique=False,nullable=False)
    

    def __init__(self,eno,name,city,designation,basic):
        self.eno=eno
        self.name=name
        self.city=city
        self.designation=designation
        self.basic=basic
    
    def serialize(self):
        return {
            'eno':self.eno,
            'name':self.name,
            'city':self.city,
            'designation':self.designation,
            'basic':self.basic
            }
    
    def __repr__(self):
        return str(self.serialize())
