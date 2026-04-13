from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # 訊息模組
from .models import House
from .forms import ContactForm

def index(request):
    """首頁：公司介紹"""
    # 這裡可以抓取最新的 3 個物件放在首頁當亮點
    featured_houses = House.objects.filter(is_sold=False).order_by('-created_at')[:3]
    return render(request, 'houses/index.html', {
        'featured_houses': featured_houses
    })

def house_list(request):
    # 1. 先從資料庫抓出「所有」物件
    houses = House.objects.all()

    # 2. 接收網址列傳來的搜尋條件 (例如使用者輸入了區域)
    search_keyword = request.GET.get('q')        # 搜尋標題
    search_location = request.GET.get('location') # 搜尋區域

    # 3. 如果有輸入條件，就進行過濾 (filter)
    if search_keyword:
        # icontains 代表「包含」這個字，且不分大小寫
        houses = houses.filter(title__icontains=search_keyword)
        
    if search_location:
        houses = houses.filter(location__icontains=search_location)

    """搜尋頁：原本的物件列表與搜尋邏輯"""
    query = request.GET.get('q')
    houses = House.objects.all()
    
    if query:
        houses = houses.filter(title__icontains=query)    

    # 4. 把過濾後的結果丟給網頁
    return render(request, 'houses/house_list.html', {'houses': houses})

# 詳情頁的部分
def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.interested_property = house
            contact.save()
            
            # 2. 加入成功訊息
            messages.success(request, f'感謝您的留言！我們將盡快與您聯絡。')
            
            # 2. 加入成功訊息
            messages.success(request, f'感謝您的留言！我們將盡快與您聯絡。')
    else:
        form = ContactForm()
    return render(request, 'houses/house_detail.html', {'house': house, 'form': form})