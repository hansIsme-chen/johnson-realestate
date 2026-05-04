from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.property_info, name='property_info'),      # 房產資訊
    path('projects/', views.house_list, name='house_list'),        # 房地產項目 (原精選物件)
    path('services/', views.services, name='services'),            # 服務
    path('activities/', views.activities, name='activities'),      # 活動
    path('house/<int:pk>/', views.house_detail, name='house_detail'),
]