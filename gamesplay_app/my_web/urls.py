from django.urls import path

from gamesplay_app.my_web.views import show_home, dashboard, profile_create, profile_edit, profile_delete, game_create, \
    profile_details, game_edit, game_delete, game_details

urlpatterns = [
    path('', show_home, name='show home'),

    path('dashboard/', dashboard, name='dashboard'),

    path('profile/create/', profile_create, name='profile create'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),
    path('profile/details/', profile_details, name='profile details'),

    path('game/create/', game_create, name='game create'),
    path('game/edit/<int:pk>/', game_edit, name='game edit'),
    path('game/delete/<int:pk>/', game_delete, name='game delete'),
    path('game/details/<int:pk>/', game_details, name='game details'),

]
