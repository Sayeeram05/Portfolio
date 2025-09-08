from flask import Flask


def createApp():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "SFSDFGSGFSDF"
    
    from .home import home
    
    app.register_blueprint(home)
    
    return app
    