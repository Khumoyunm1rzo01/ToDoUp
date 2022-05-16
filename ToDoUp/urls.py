
from django.contrib import admin
from django.urls import path
from Main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('change-status/<int:pk>/', changestatus, name='change-status'),
    path('passive-todos/', passivetodos , name='passive-todos'),
    path('status/', status , name='status'),
    path('active/', activetodos, name='active'),
    path('delete-todo/<int:pk>/', deletetodo , name='delete-todo'),
    path('change-task', changetask, name='change-task')
]
