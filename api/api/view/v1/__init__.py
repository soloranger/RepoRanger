from flask import Blueprint
from flask_restful import Api

from .repository import RepositoryResource

api_bp = Blueprint("apiv1_bp", __name__, url_prefix="/api/v1")
api = Api(api_bp)

api.add_resource(
    RepositoryResource,
    "/repositories",
    methods=["GET", "POST"],
    endpoint="apiv1_repositories",
)

api.add_resource(
    RepositoryResource,
    "/repositories/<repository_id>",
    methods=["GET", "PATCH", "DELETE"],
    endpoint="apiv1_repository",
)
