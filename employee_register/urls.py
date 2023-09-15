from django.urls import path,include
from . import views

urlpatterns = [
    path("insert/", views.employee_form,name="employee_insert"),
    path("<int:id>/",views.employee_form,name="employee_update"),
    path("delete/<int:id>/",views.employee_delete,name="employee_delete"),
    path("list/",views.employee_list, name="employee_list")
]
