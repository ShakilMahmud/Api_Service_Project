from django.contrib import admin
from django.urls import path
from api.views import UserLonginView,UserLogoutView,DataInputView
urlpatterns = [
  path('login/',UserLonginView.as_view(),name="login"),
  path('logout/',UserLogoutView.as_view(),name="logout"),
  path('',DataInputView.as_view(),name="data"),
  #path('we/',test),

]
