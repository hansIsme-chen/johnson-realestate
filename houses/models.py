from django.db import models

# 房屋物件模型
class House(models.Model):
    title = models.CharField(max_length=200, verbose_name="物件標題")
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="總價(元)")
    address = models.CharField(max_length=255, verbose_name="詳細地址")
    description = models.TextField(verbose_name="物件描述")
    rooms = models.IntegerField(default=3, verbose_name="房間數")
    bathrooms = models.IntegerField(default=2, verbose_name="衛浴數")
    square_feet = models.IntegerField(default=40, verbose_name="坪數")
    is_sold = models.BooleanField(default=False, verbose_name="是否已售出")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='house_photos/', null=True, blank=True, verbose_name="房屋照片") # 新增圖片欄位：upload_to 會自動建立資料夾

    CATEGORY_CHOICES = [
        ('project', '新開案'),
        ('subsale', '中古屋'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='subsale', verbose_name="物件類別")
    
    # 增加硬體規格
    bathrooms = models.IntegerField(default=1, verbose_name="衛浴數")
    square_feet = models.IntegerField(default=0, verbose_name="坪數/平方英尺")
    
    # 增加地點標籤（用於篩選）
    location = models.CharField(
    max_length=100, 
    default='台北', # 幫以後的新資料也設定預設值
    verbose_name="區域"
)

    def __str__(self):
        return self.title

# 訪客聯絡資料模型
class VisitorContact(models.Model):
    name = models.CharField(max_length=100, verbose_name="訪客姓名")
    phone = models.CharField(max_length=20, verbose_name="聯絡電話")
    message = models.TextField(verbose_name="留言內容")
    # 關連到 House 模型
    interested_property = models.ForeignKey(
        House, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="感興趣的物件"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"