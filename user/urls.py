from . import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('login', views.loginView.as_view(), name="login"),
    path('register', views.registerView.as_view(), name="register"),
    path('userList', views.userListView.as_view(), name="userList"),
    path('<user>/dashboard', views.dashboardView.as_view(), name="dashboard"),
    path('<user>/requestDonor', views.requestDonorView.as_view(), name="requestDonor"),
    path('<user>/requestOrganizer',views.requestOrganizerView.as_view(), name="requestOrganizer"),
]
