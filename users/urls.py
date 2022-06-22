from django.urls import path
from . import views
urlpatterns=[
    path("signin/",views.SignUpView.as_view(),name='signin')
]