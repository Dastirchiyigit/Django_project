from django.urls import path
from . import views

urlpatterns =[

path("<topic>",views.one_func_to_all),
    
]