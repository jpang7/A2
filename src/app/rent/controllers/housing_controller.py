from . import *
d = {'success':'true'}

@rent.route('/', methods = ['GET'])
def testing():
    return jsonify("Hello World")

@rent.route('/allhouses', methods = ['GET', 'POST', 'DELETE'])
def get_all():
    li = []
    houses = Housing.query.all()
    for h in houses:
        di = {}
        di['propertyName'] = h.propertyName
        di['propertyPrice']=h.propertyPrice
        di['propertyLocation']=h.propertyLocation
        di['propertyAddress']=h.propertyAddress
        di['ownerName']=h.ownerName
        di['propertyLatitude']=h.propertyLatitude
        di['propertyLongitude']=h.propertyLongitude
        li.append(di)
    return jsonify(li)
    #t = db.get_all()
    #return jsonify(t)

@rent.route('/test/<name>')
def test_name(name):
    return jsonify('this is the name' + name)

@rent.route('/createhouse/<name>/<price>/<location>/<address>/<ownerName>/<latitude>/<longitude>', methods = ['GET', 'POST', 'DELETE'])
def create_house(name,price,location,address,ownerName,latitude,longitude):
    try:
        house = Housing(name, price, location, address, ownerName, latitude, longitude)
        db.session.add(house)
        db.session.commit()
        return jsonify(d)
    except Exception as e: print e
   

@rent.route('/delete/<name>', methods = ['GET', 'POST', 'DELETE'])
def delete_house(name):
    dhouse = Housing.query.filter_by(propertyName = name).first()
    db.session.delete(dhouse)
    db.session.commit()
    return jsonify(d)

@rent.route('/deleteall', methods = ['GET', 'POST', 'DELETE'])
def delete_all():
    houses = Housing.query.all()
    for h in houses:
        db.session.delete(h)
    db.session.commit()
    return jsonify(d)
    