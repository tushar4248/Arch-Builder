from flask import Blueprint,jsonify, render_template

# Create a blueprint for routes
hello_world_bp = Blueprint('hello_world', __name__)
# Create a blueprint for routes
item_list_bp = Blueprint('item_list', __name__)
# Create a blueprint for routes
proj_list_bp = Blueprint('proj_list', __name__)

# Define a route to return "Hello World"
@hello_world_bp.route('/')
def hello_world():
    return 'Hello World'


# Define a route to return a list of items
@item_list_bp.route('/items')
def get_items():
    items = ['Item 1', 'Item 2', 'Item 3']  # Replace with your list of items
    return jsonify(items)

# Define a route to render the proj_list.html template
@proj_list_bp.route('/proj_list')
def proj_list():
    return render_template('proj_list.html')

