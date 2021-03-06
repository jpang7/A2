from . import *

class Housing(Base):
  __tablename__ = 'housing'

  #house_id = db.Column(db.Integer, db.ForeignKey('house.id'), unique =True, index =True)
  house_id = db.Column(db.Integer, primary_key=True)
  propertyName = db.Column(db.String(128), nullable =False, unique = True)
  propertyPrice = db.Column(db.String(128), nullable = False)
  propertyLocation = db.Column(db.String(128))
  propertyAddress = db.Column(db.String(128), unique=True)
  ownerName = db.Column(db.String(128))
  propertyLatitude = db.Column(db.String(128))
  propertyLongitude = db.Column(db.String(128))
  #TODO, change quantities of strings, implement id
                  

  def __init__(self, name, price, loc, add, oname, lat, long):
    #self.house_id = kwargs.get('house_id',None)
    #self.house_id = 
    self.propertyName = name
    self.propertyPrice = price
    self.propertyLocation = loc
    self.propertyAddress = add
    self.ownerName = oname
    self.propertyLatitude = lat
    self.propertyLongitude = long
    """
    self.propertyName = kwargs.get('propertyName',None)
    self.propertyPrice = kwargs.get('propertyPrice',None)
    self.propertyLocation = kwargs.get('propertyLocation',None)
    self.propertyAddress = kwargs.get('propertyAddress',None)
    self.ownerName = kwargs.get('ownerName',None)
    self.propertyLatitude = kwargs.get('propertyLatitude',None)
    self.propertyLongitude = kwargs.get('propertyLongitude',None)
    """

  def __repr__(self):
    return str(self.__dict__)
    

