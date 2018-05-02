from django.conf.urls import url
from . import views

# create urls

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
