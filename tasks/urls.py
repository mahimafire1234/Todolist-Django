from . import views
from django.urls import path

urlpatterns=[
    path("",views.home),
    path("login",views.login),
    path("forcreate",views.create),
    path("create",views.index),
    path("update/<int:pk>",views.update,name="update_task"),
    path("delete/<int:pk>", views.delete, name="delete_task")
]