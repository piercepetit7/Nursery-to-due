from django.urls import path
from .views import DueList, DueDetail, DueCreate, DueUpdate, DueDelete

urlpatterns = [
  path('', DueList.as_view(), name='task'),
  # path('accounts/signup/', views.signup, name='signup'),
  path('task/<int:pk>/', DueDetail.as_view(), name='task'),
  path('task/new/', DueCreate.as_view(), name='task_new'),
  path('task/<int:pk>/edit/', DueUpdate.as_view(), name='task_edit'),
  path('task/<int:pk>/delete/', DueDelete.as_view(), name='task_delete'),
]

