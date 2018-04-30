from flask import jsonify, request, make_response, Blueprint

from models_v1.models import DbOrders

orders_db = DbOrders()

orders = Blueprint('orders', __name__, url_prefix='/api/v1')

@orders.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    try:
        if data['caterer'] and data['meal']:
            new_order = orders_db.add_order('default', data['caterer'], data['meal'])

            if new_order:
                message = 'Order {} successfully placed.'.format(data)
                return make_response(jsonify(message=message), 201)
    except KeyError:
        pass
    return make_response(jsonify(message='Invalid request format'), 403)


@orders.route('/orders/<int:meal_id>', methods=['PUT'])
def modify_order(meal_id):
    data = request.get_json()
    try:
        if data['caterer'] and data['meal']:
            new_order = orders_db.modify_order(customer='default', caterer=data['caterer'], order_id=meal_id, meal=data['meal'])

            if new_order:
                message = 'Order {} successfully placed.'.format(data)
                return make_response(jsonify(message=message), 201)
    except KeyError:
        pass
    return make_response(jsonify(message='Invalid request format'), 403)


@orders.route('/orders', methods=['GET'])
def get_all_orders():
    orders_per_caterer = orders_db.get_orders(caterer='default4')
    if orders_per_caterer:
        message = 'The request was successfull'
        return make_response(jsonify(message=message, content=orders_per_caterer), 200)
    return make_response(jsonify(message='Oops, orders not found.'), 200)

