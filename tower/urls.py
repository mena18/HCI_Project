from django.urls import path
from .views import *

app_name="tower"
# or  namespace='blog') inside the url to that file


urlpatterns = [
    path('',home,name='home'),

    path('engineer/workers',engineer_workers,name="engineer_workers"),

    path('test/table',table_test,name='table'),
    path('test/pdf',pdf_view,name='pdf'),
]
