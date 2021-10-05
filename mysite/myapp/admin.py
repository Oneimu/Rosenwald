from django.contrib import admin


class MyAppConfig(AppConfig):
    default_auto_field =  'djang.db.models.BigAutoField'
    name = 'myapp'
# Register your models here.
