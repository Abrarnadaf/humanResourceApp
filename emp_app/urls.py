from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index , name='index'),
    path('all_emp', views.all_emp , name='all_emp'),
    path('add_emp', views.add_emp , name='add_emp'),
    path('remove_emp', views.remove_emp , name='remove_emp'),
    path('remove_emp/<int:employee_id>', views.remove_emp , name='remove_emp'),
    path('filter_emp', views.filter_emp , name='filter_emp'),
    path('emp_report', views.emp_report , name='emp_report'),
    path('add_attendance/<int:empid>', views.add_attendance, name='add_attendance'),
    path('show_employee_details/<int:empid>', views.show_employee_details, name='show_employee_details'),

]