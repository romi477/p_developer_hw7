from django.urls import path
from .views import *
# from django.conf import settings
# from django.conf.urls.static import static
#


urlpatterns = [
    path('add/', CreateTest.as_view(), name='add_obj'),
    path('signup/', signup, name='signup'),
    path('registration/', RegistrationFormView.as_view(), name='registration'),
    # path('registration/validate-email/', validate_email, name='validate_email'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogOutFormView.as_view(), name='logout'),
    # path('editprofile/', EditUserForm.as_view(), name='edit_profile')
]