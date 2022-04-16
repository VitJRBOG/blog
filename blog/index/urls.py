from django.urls import include, path


urlpatterns = [
    path('articles/', include('articles.urls')),
    path('comments/', include('comments.urls'))
]