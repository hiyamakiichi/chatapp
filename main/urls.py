from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),  # 第 2 引数を変更。元々あるコードを書き換えてください。
    path("friends/", views.friends, name="friends"),
    path("talk_room/<user_id>", views.talk_room, name="talk_room"),
    path("settings/", views.settings, name="settings"),

]

