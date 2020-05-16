from . import views
from django.urls import path
app_name= 'creations'


urlpatterns=[

    path('',views.portfolio,name="portfolio"),
]