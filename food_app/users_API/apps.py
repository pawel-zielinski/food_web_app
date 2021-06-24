from django.apps import AppConfig


class UsersApiConfig(AppConfig):
    name = 'users_API'

    def ready(self):
        import users_API.signals
