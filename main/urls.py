from django.urls import path, include
# from main.views import TaskListCreateAPIView

app_name = 'main'
urlpatterns = [
    # path('tasks/', TaskListCreateAPIView.as_view(), name='tasks')
    path('', include('main.router'), name='task')
]
