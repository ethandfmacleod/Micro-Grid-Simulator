from typing import List
from ninja import Router
from ninja_crud import views, viewsets
from objects.schemas.ProjectSchemas import *

router = Router()

class ProjectViewSet(viewsets.APIViewSet):
    from objects.models.Project import Project
    
    router = router
    model = Project

    list_departments = views.ListView(response_body=List[ProjectSchema])
    create_department = views.CreateView(request_body=ProjectCreateSchema, response_body=ProjectSchema)
    read_department = views.ReadView(response_body=ProjectSchema)
    update_department = views.UpdateView(request_body=ProjectPatchSchema, response_body=ProjectSchema)
    delete_department = views.DeleteView()
    