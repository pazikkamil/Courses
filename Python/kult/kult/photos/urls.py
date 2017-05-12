from django.conf.urls import url
from photos import views as photos_views

urlpatterns = [
    url(r'^dashboard/', photos_views.dashboard, name="dashboard")
]