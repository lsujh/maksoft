from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import collaborator_view, cabinet_view, company_view, additional_office_view, menu

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='admin/login.html',
                                           extra_context={'title': 'Login',
                                                          'site_title': 'My Site',
                                                          'site_header': 'My Site Login'}),
         name='login'),
    path('logout/', LogoutView.as_view()),
    path('collaborator/', collaborator_view, name='collaborator'),
    path('cabinet/', cabinet_view, name='cabinet'),
    path('company/', company_view, name='company'),
    path('additional_office/', additional_office_view, name='additional_office'),
    path('', menu, name='menu'),
]

