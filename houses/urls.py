from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),               # 首頁 (公司介紹)
    path('houses/', views.house_list, name='house_list'), # 物件搜尋頁
    path('house/<int:pk>/', views.house_detail, name='house_detail'),
]