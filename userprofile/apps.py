from django.apps import AppConfig


class UserprofileConfig(AppConfig):
    name = 'userprofile'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
