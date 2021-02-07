from django.urls import path
from . import views
from .views import (
    PostListView,
    PostCreateView
)

urlpatterns = [
    # path('', views.criteria, name='scheduler-criteria'),
    # path('test/', views.test, name='scheduler-test'),
    path('', PostListView.as_view(), name='criteria-list'),
    path('criteria/', PostCreateView.as_view(), name='criteria-create'),
]
