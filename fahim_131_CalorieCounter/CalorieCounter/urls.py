from django.urls import path
from CalorieCounter.views import *

urlpatterns = [
    path('', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('dashboard/', dashboard_page, name='dashboard_page'),
    path('profile/', profile_page, name='profile_page'),
    path('update-profile/', update_profile, name='update_profile'),
    path('add-consumed-calorie/', consumed_calories_list, name='consumed_calories_list'),
    path('add-calorie/', add_calorie, name='add_calorie'),
    path('update-calorie/<str:t_id>/', update_calorie, name='update_calorie'),
    path('delete-calorie/<str:t_id>/', delete_calorie, name='delete_calorie'),
]
