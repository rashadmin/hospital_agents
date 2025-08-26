from flask import Flask
from config import Config
from app.errors import bp as errors_bp
from app.agent_call import bp as agent_call_bp
def create_app(config_class=Config):    
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(errors_bp)
    app.register_blueprint(agent_call_bp,url_prefix='/agent_call')
    return app

from app.agent_call import routes