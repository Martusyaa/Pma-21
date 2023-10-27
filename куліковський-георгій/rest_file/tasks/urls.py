from django.urls import path

from .views import (Tasks_List, Tasks_Create, Tasks_Update, Tasks_Delete, Tasks_Complete,
    Tasks_List_Unfinished, Tasks_List_Finished)

urlpatterns = [
    #get all tasks
    path('api/tasks-get/', Tasks_List.as_view(), name='tasks'),
    #get unfinished tasks only
    path('api/tasks-get-unfinished/', Tasks_List_Unfinished.as_view(), name='tasks-unfinished'),
    #get finished tasks only
    path('api/tasks-get-finished/', Tasks_List_Finished.as_view(), name='tasks-finished'),

    #put
    path('api/tasks-update/<int:pk>/', Tasks_Update.as_view(), name='tasks-update'),
    #post
    path('api/tasks-create/', Tasks_Create.as_view(), name='tasks-create'),
    #delete
    path('api/tasks-delete/<int:pk>/', Tasks_Delete.as_view(), name='tasks-delete'),
    #patch
    path('api/tasks-complete/<int:pk>/', Tasks_Complete.as_view(), name='tasks-complete')
]
