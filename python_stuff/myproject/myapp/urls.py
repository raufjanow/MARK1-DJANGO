from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('',views.hello_view, name ='hello')
]
