from django.urls import include, path
#from rest_framework_simplejwt import views as jwt_views
from .views import SchedulerUserCreate

urlpatterns = [
#    path('create/', SchedulerUserCreate.as_view(), name="create_user"),
#    path('obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # overrides stock token
#    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]