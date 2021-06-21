from django.urls import path
from . import views

urlpatterns = [
    path('testapi',views.testapi,name='testapi'),
    path('emotionapi',views.emotionapi,name='emotionapi'),
    path('guideapi',views.guideapi,name='guideapi'),
    path('dbapi',views.dbapi,name='dbapi'),
]