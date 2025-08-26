from flask import Blueprint

bp = Blueprint('agent_calls', __name__)

from app.agent_call import routes,external,graph