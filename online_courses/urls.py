
from django.urls import path
from online_courses import views




# app_name = 'online_courses'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('Logout', views.user_logout, name='logout'),
    path('login',views.user_login, name='login'),
    path('categories/', views.categories, name='categories'),
    path('categories/maths/', views.maths, name='maths'),
    path('categories/<int:course_id>/', views.course, name='course'),
    path('categories/english/', views.english, name='english'),
    path('register/', views.register, name='register'),
]