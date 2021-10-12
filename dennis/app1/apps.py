from django.apps import AppConfig


class App1Config(AppConfig):
    name = 'app1'
    def ready(self):
        import app1.signals
