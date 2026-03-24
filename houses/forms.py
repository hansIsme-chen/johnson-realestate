from django import forms
from .models import VisitorContact

class ContactForm(forms.ModelForm):
    class Meta:
        model = VisitorContact
        # 我們只需要訪客填這三個，其餘的（如：感興趣的物件、時間）我們會用程式自動填入
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '您的姓名'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '聯絡電話'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '我想詢問...'})
        }