from ninja import ModelSchema, Schema
from objects.models.Project import Project

class ProjectSchema(ModelSchema):
    class Meta:
        model = Project
        fields = "__all__"

class ProjectPatchSchema(ModelSchema):
    class Meta:
        model = Project
        fields = ['name']
        fields_optional = ['name']

# Create and Delete dont require any information from the request body
class ProjectCreateSchema(Schema):
    pass

class ProjectDeleteSchema(Schema):
    pass