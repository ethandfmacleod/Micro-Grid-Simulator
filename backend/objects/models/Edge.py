from django.db import models

class Edge(models.Model):
    project = models.ForeignKey("flowsheet.Project", on_delete=models.CASCADE, related_name='project_edges')
    source = models.ForeignKey("Node", on_delete=models.CASCADE, related_name="from_node")
    target = models.ForeignKey("Node", on_delete=models.CASCADE, related_name="to_node")