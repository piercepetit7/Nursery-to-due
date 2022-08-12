from django.urls import path
from .views import DueList, DueDetail, DueCreate, DueUpdate, DueDelete, MyLoginView, SignUpPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
  path('login/', MyLoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
  path('sign_up/', SignUpPage.as_view(), name='sign_up'),
  path('', DueList.as_view(), name='task'),
  path('task/<int:pk>/', DueDetail.as_view(), name='task'),
  path('task/new/', DueCreate.as_view(), name='task_new'),
  path('task/<int:pk>/edit/', DueUpdate.as_view(), name='task_edit'),
  path('task/<int:pk>/delete/', DueDelete.as_view(), name='task_delete'),
]

