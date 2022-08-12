from django.urls import path
from .views import DueList, DueDetail, DueCreate

urlpatterns = [
  path('', DueList.as_view(), name='task'),
  # path('accounts/signup/', views.signup, name='signup'),
  path('task/<int:pk>/', DueDetail.as_view(), name='task'),
  path('task/new/', DueCreate.as_view(), name='task_new'),

]

