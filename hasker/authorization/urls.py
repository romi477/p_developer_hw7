from django.urls import path
from .views import *


urlpatterns = [
    path('registration/', RegistrationFormView.as_view(), name='registration'),
    path('registration/validate-email/', validate_email, name='validate_email'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogOutFormView.as_view(), name='logout'),

]