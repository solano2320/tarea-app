from django.urls import path
from . import views  

urlpatterns = [
    path('add/', views.AddComment.as_view(), name='add_comment'),
    path('view/', views.ViewComments.as_view(), name='view_coment'),
    path('views/<str:name>/', views.ViewsComents.as_view(), name='views_coment'),
    path('delete/', views.DeleteComents.as_view(), name='delete_coment'),
    path('deletes/<str:name>', views.DeleteComent.as_view(), name='deletes_coment'),
]
