from flask import Flask

def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    # Register Blueprints
    from .routes import hello_world_bp,item_list_bp,proj_list_bp
    app.register_blueprint(hello_world_bp)
    app.register_blueprint(item_list_bp)
    app.register_blueprint(proj_list_bp)


    return app
