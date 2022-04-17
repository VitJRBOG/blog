from django.urls import path
from . import view


urlpatterns = [
    path('add', view.add),
    path('get', view.get),
    path('delete', view.delete)
]
