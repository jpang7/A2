from . import *
d = {'success':'true'}


@rent.route('/', methods = ['GET'])
def testing():
    return jsonify("Hello World")

@rent.route('/allhouses', methods = ['GET'])
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

@rent.route('/createhouse', methods = ['POST'])
def create_house():
    housing = Housing()
    #name = request.args['name']
    #location = request.args['location']
    #reviews = request.args['reviews']
    #housing = Housing(name,reviews, location)
    #db.create_house(housing)
    #return jsonify(task.to_dict())

#@app.route('/deletehouse', methods = ['DELETE'])
#def delete_house():
    
    #house_id = request.args.get('id')
    #t = db.delete_house(house_id)
    #return jsonify(d)