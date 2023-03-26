
from django.urls import path
from .views import *

urlpatterns = [
   path('task_url',task_url,name='tas_kurl'),
   path('get_task/',get_task,name='get_task'),
   path('taskDetalis/<id>/',taskDetalis,name='taskDetalis'),
   path('taskCreate/',taskCreate,name='taskCreate'),
   path('taskUpdate/<id>/',taskUpdate,name='taskUpdate'),
   path('tast_delcet/<id>/',tast_delcet,name='tast_delcet'),
]
