from django import forms
from . import models

"""CATEGORY_CHOICES = [
    ('music','music'),
    ('species','species'),
    ('physical activity','physical activity'),
    ('food','food'),
    ('others','others'),
]"""

class CreateArticle(forms.ModelForm):
    class Meta:
        model= models.Article
        fields=['title','body','slug','thumb']
        
    #category=forms.CharField(label='Category', widget=forms.Select(choices=CATEGORY_CHOICES))
