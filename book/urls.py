from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^registration$',views.Registration_User,name='Registration_User'),
    url(r'^thanks$',views.Thanks_User,name='Thanks_User'),
]
