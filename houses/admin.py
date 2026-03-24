from django.contrib import admin
from .models import House, VisitorContact

# 在後台顯示更詳細的表格
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_sold', 'created_at')
    search_fields = ('title', 'address')

@admin.register(VisitorContact)
class VisitorContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'interested_property', 'created_at')