from flask import Flask


def createApp():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "SFSDFGSGFSDF"
    
    from .view import view
    
    app.register_blueprint(view)
    
    return app
    