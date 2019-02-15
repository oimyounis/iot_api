from django.urls import path
from .webhooks import index


app_name = 'api'

urlpatterns = [
    path('', index, name='index')
]
