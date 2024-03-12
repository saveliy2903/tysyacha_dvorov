from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add-application/', views.add_application, name="add_applic"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('view-application/', views.view_applic, name="view_applic"),
    path('view-application/delete/<int:id>/', views.delete_applic),
]