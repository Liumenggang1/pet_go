
from django.urls import path,include
from pet import views
app_name = 'pet'
urlpatterns = [
    path('',views.home,name='home'),
    path('my_pet/',views.my_pet,name='my_pet'),
    path('pets/add/', views.add, name='add'),
    path('pets/<int:pet_id>/delete/', views.pet_delete, name='pet_delete'),
    path('task/add/',views.task_add,name='task_add'),
    path('task/list/',views.task_list,name='task_list'),
    path('task/<int:task_id>',views.task,name='task'),

    path('my_task/list',views.my_task_list,name='my_task_list'),
    path('my_task/<int:my_task_id>',views.my_task,name='my_task'),

]
