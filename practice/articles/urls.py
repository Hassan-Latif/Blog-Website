from django.contrib import admin
from django.urls import path,re_path
from . import views

app_name='articles'

urlpatterns = [
  #  path('admin/', admin.site.urls),
    path(r'',views.article_list),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail,name='details'),
]
