
from django.urls import path

from testapp.views.sync import index_view

urlpatterns = [
    path('', index_view, name='index'),
]