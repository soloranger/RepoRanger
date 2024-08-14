from flask_restful import Resource

from api.controller.v1 import RepositoryController


class RepositoryResource(Resource):
    def get(self, repository_id=None):
        # GET /api/v1/repositories -> Repository List.
        # GET /api/v1/repositories/<repository_id> -> Get Repository
        if repository_id is None:
            return RepositoryController.get_repositories()
        else:
            return RepositoryController.get_repository(repository_id)

    def post(self):
        # POST /api/v1/repositories -> Create New Repository .
        # POST /api/v1/repositories/<repository_id> -> Not Allowd
        return RepositoryController.create_repository()

    def patch(self, repository_id):
        # PATCH /api/v1/repositories -> Not Allowd
        # PATCH /api/v1/repositories/<repository_id> -> Update an existing repository
        return RepositoryController.update_repository(repository_id)

    def delete(self, repository_id):
        # DELETE /api/v1/repositories -> Not Allowd
        # DELETE /api/v1/repositories/<repository_id> -> Delete  an existing repository
        return RepositoryController.delete_repository(repository_id)
