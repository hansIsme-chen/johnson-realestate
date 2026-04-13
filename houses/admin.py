from django.contrib import admin
from .models import House, HouseImage, VisitorContact

class HouseImageInline(admin.TabularInline):
    model = HouseImage
    extra = 3  # 預設多給 3 個上傳框

# 在後台顯示更詳細的表格
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseImageInline]  # 將圖片上傳內嵌進來
    list_display = ('title', 'price', 'is_sold', 'created_at', 'cover_image')
    search_fields = ('title', 'address')

@admin.register(VisitorContact)
class VisitorContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'interested_property', 'created_at')

    