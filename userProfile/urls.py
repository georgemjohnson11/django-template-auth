from django.urls import include, path

from .views import UserProfileListView

urlpatterns = [
    path('', UserProfileListView.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls'))
]