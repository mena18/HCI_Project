from django.urls import path
from .views import *

app_name="tower"
# or  namespace='blog') inside the url to that file


urlpatterns = [
    path('',home,name='home'),
    path('table',table_test,name='table'),
    path('pdf',pdf_view,name='pdf'),
]
