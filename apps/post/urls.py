from django.urls import path
from apps.post.views import add_task, signup, task_detail, task_list, user_login, user_logout


urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('tasks/add/', add_task, name='add_task'),
    path('tasks/<int:task_id>/', task_detail, name='task_detail'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    
]