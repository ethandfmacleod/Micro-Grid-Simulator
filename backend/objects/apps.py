from django.apps import AppConfig

class ObjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'objects'
    label = 'objects'

    def ready(self):
        import objects.signals
