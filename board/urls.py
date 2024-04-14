from django.urls import path
from .views import ItemLV,content_comment,ItemCV,ItemDeleteView,itemLV,test1,test

app_name = 'spring'

urlpatterns = [
    path('',ItemLV.as_view(),name='index'),
    path('detail/<int:pk>',content_comment,name='detail'),
    path('create/',ItemCV.as_view(),name='create'),
    path('delete/<int:pk>',ItemDeleteView.as_view(),name='delete'),
    
    path('f/',itemLV),
    path('lion/<int:pk>/',test1),
    path('lion/tiger/',test),
]