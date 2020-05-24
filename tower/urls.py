from django.urls import path
from .views import *

app_name="tower"
# or  namespace='blog') inside the url to that file


urlpatterns = [
    path('',home,name='home'),

    path('test/add_workers',add_workers,name="test_add_workers"),
    path('test/add_operations',add_operations,name="test_add_operations"),

    path("engineer/home",engineer_home,name="engineer_home"),
    path('engineer/workers',engineer_workers,name="engineer_workers"),
    path("engineer/foremen",engineer_foremen,name="engineer_foremen"),
    path("engineer/levels",engineer_levels,name="engineer_levels"),
    path("engineer/level/<int:num>",engineer_level,name="engineer_level"),

    path("foreman/home",foreman_home,name="foreman_home"),
    path('forman/levels',foreman_levels,name="foreman_levels"),
    path('forman/levels/<int:num>',foreman_levels,name="foreman_level"),

    path("worker/home",worker_home,name="worker_home"),

]
