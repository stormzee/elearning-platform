
from django.urls import path
from online_courses import views




# app_name = 'online'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('courses/maths/', views.maths, name='maths'),
]