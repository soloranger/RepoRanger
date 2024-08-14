from api.model import Repository
from api.object import db
from api.schema.v1 import RepositorySchema
from api.util import jsonify, now
from flask import request



class RepositoryController:
    def get_repositories():
        try:
            repositories = Repository.query.all()
        except:
            return jsonify(status=500, code=102)
        try:
            repositories_schema = RepositorySchema(many=True)
        except:
            return jsonify(status=500, code=103)
        return jsonify(repositories_schema.dump(repositories))

    def get_repository(repository_id):
        try:
            repository = Repository.query.get(repository_id)
        except:
            return jsonify(status=500, code=102)
        if repository is None:
            return jsonify(status=404, code=105)
        try:
            repository_schema = RepositorySchema()
        except:
            return jsonify(status=500, code=103)

        return jsonify(repository_schema.dump(repository))

    def create_repository():
        try:
            repository_schema = RepositorySchema(partial=True)
        except:
            return jsonify(status=500, code=103)
        try:
            request_data = repository_schema.load(request.get_json())
        except:
            return jsonify(status=400, code=104)

        repository = Repository(owner="TBC", url=request_data["url"])
        db.session.add(repository)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)
        return jsonify(repository_schema.dump(repository), status=201)

    def update_repository(repository_id):
        try:
            repository = Repository.query.get(repository_id)
        except:
            return jsonify(status=500, code=102)
        if repository is None:
            return jsonify(status=404, code=105)
        
        try:
            repository_schema = RepositorySchema(only=["status"])
        except:
            return jsonify(status=500, code=103)
        try:
            request_data = repository_schema.load(request.get_json())
        except:
            return jsonify(status=400, code=104)

        repository.status = request_data["status"]
        repository.last_updated_at = now()
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)
        try:
            repository_schema = RepositorySchema(only=["status"])
        except:
            return jsonify(status=500, code=103)
        
        return jsonify(repository_schema.dump(repository), status=200)
        
    def delete_repository(repository_id):
        return jsonify(status=501, code=101)
