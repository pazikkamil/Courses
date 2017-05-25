from django.conf.urls import url
from photos import views as photos_views


app_name = 'photos'

urlpatterns = [
    url(r'^dashboard/', photos_views.dashboard, name="dashboard")
]