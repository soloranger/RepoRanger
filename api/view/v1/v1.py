from flask import Blueprint 
from flask_restful import Api


apiv1_bp = Blueprint("apiv1_bp",__name__,url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)
