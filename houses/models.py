from django.db import models

# 房屋物件模型
class House(models.Model):
    title = models.CharField(max_length=200, verbose_name="物件標題")
    price = models.CharField(max_length=100, verbose_name="價格區間", help_text="勾選下方時填寫數字即可(如: 100-500)；不勾選時請填寫完整格式(如: 10000000)")
    is_starting_price = models.BooleanField(default=True, verbose_name="是否顯示『萬起』")
    address = models.CharField(max_length=255, verbose_name="詳細地址")
    description = models.TextField(verbose_name="物件描述")
    rooms = models.CharField(max_length=50, default=3, verbose_name="房間數", help_text="可以填寫範圍，例如：1-3")
    bathrooms = models.CharField(max_length=50, default=2, verbose_name="衛浴數", help_text="可以填寫範圍，例如：2-3")
    square_feet = models.IntegerField(default=40, verbose_name="坪數")
    is_sold = models.BooleanField(default=False, verbose_name="是否已售出")
    created_at = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='houses/covers/', blank=True, null=True, verbose_name="主圖")

    # --- 以下是從下面搬上來的欄位，房子才有類別跟區域 ---
    CATEGORY_CHOICES = [
        ('project', '新成屋'),
        ('subsale', '中古屋'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='subsale', verbose_name="物件狀態")
    location = models.CharField(max_length=100, default='台北', verbose_name="區域")

    def __str__(self):  # 正確的寫法是 __str__
        return self.title

# 房屋照片模型 (專門存多張圖)
class HouseImage(models.Model):
    house = models.ForeignKey(House, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='houses/gallery/', verbose_name="上傳照片")
    alt_text = models.CharField(max_length=200, blank=True, help_text="照片描述（例如：客廳、主臥）")

    def __str__(self):
        # 這裡只留一個，並且確保它是抓 house 的 title
        return f"{self.house.title} 的照片"

# 訪客聯絡資料模型
class VisitorContact(models.Model):
    name = models.CharField(max_length=100, verbose_name="訪客姓名")
    phone = models.CharField(max_length=20, verbose_name="聯絡電話")
    message = models.TextField(verbose_name="留言內容")
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