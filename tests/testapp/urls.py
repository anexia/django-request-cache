from django.urls import path

from testapp.views.sync import index_view, pandas_view

urlpatterns = [
    path('', index_view, name='index'),
    path('pandas_dataframe/', pandas_view, name='pandas_dataframe'),
]
