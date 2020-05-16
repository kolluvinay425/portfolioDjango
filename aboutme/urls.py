from . import views
from django.urls import path
app_name = 'aboutme'


urlpatterns =[


    path('',views.about,name="about")
]