from django.urls import include, path
from . import view


urlpatterns = [
    path('add', view.add),  # type: ignore
    path('get', view.get),  # type: ignore
    path('delete', view.delete)  # type: ignore
]
