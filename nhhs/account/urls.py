from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

app_name="account"
urlpatterns = [
    path('register/', views.reg, name="reg"),

    path('', views.main, name="main-page"),

    path('login/', views.log, name="log"),

    path('about/', views.about, name="about"),


     path('health_care/', views.health, name="health"),
      path('child_education/', views.child, name="child"),
       path('homeless_persion/', views.homeless, name="homeless"),



    path('donate_section/', views.section, name="Donate Sections"),

    path('news/', views.home, name="news-page"),
    path('members/', views.memList, name="mem-list"),
    path('donorform/', views.donateChildEdu, name="donate-child-education"),
    path('search/', views.search, name="search-mem"),
    path('upload/', views.upload, name="upload"),
    #path('upload_list/', views.upload_list, name="upload-list"),
    
    #path('upload/<int:pk>/', views.delete_photo, name="delete_photo"), 
    path('logout/', views.logout, name="logout"),
    path('/<int:pk>/', views.deletecreation, name='deletecreation'),

    path('api/upload/<int:pk>/', views.update_api_data, name="update_api_data"),
    path('api/', views.read_api_data, name="read_api_data"),

    path('upload_pegination/<int:PAGENO>/<int:SIZE>/', views.upload_pegination, name="upload_pegination"),




    
    
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
