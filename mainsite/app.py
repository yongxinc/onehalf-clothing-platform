from django.apps import AppConfig
class PaymentConfig(AppConfig):
    name = 'mainsite'
    verbose_name = 'Mainsite'
    def ready(self):
        import mainsite.signal