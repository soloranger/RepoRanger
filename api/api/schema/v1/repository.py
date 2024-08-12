from api.model import Repository
from api.object import ma


class RepositorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Repository

    id = ma.auto_field(dump_only=True)  # Just Can see it and Cant modify it
    owner = ma.auto_field(dump_only=True)
    url = (
        ma.auto_field()
    )  # if we dont set anything => also can see it and can Modify it
    created_at = ma.auto_field(dump_only=True)
    last_updated_at = ma.auto_field(dump_only=True)
    status = ma.auto_field(dump_only=True)
