from django.urls import path
from django.urls.resolvers import URLPattern
from .views import SignUpView,ProfileUpdate,EmailUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(),name= "signup"),
    path('profile/', ProfileUpdate.as_view(),name= "profile"),
    path('profile/email/', EmailUpdate.as_view(),name= "profile-email"),
]