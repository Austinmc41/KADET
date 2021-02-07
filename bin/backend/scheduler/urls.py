from django.urls import path
from . import views
from .views import (
    V2ListView,
    V2CreateView,
    V2UpdateView,
    V2DetailView
)

urlpatterns = [
    # path('', views.criteria, name='scheduler-criteria'),
    # path('test/', views.test, name='scheduler-test'),
    path('', V2ListView.as_view(), name='criteria-list'),
    path('criteria/<int:pk>/', V2DetailView.as_view(), name='criteria-detail'),
    path('criteria/', V2CreateView.as_view(), name='criteria-create'),
    path('criteria/<int:pk>/edit', V2UpdateView.as_view(), name='criteria-update'),
]
