from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^mainpage$',views.mainPage,name='main_page'),
    url(r'^infopage$',views.infoPage,name='info_page'),
]
