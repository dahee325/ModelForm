# MODELFORM
-  데이터와 데이터를 입력받을 수 있는 폼을 합쳐놓은 것

## 00.settings
- `python -m venv venv`
- `source venv/Scripts/activate`
- `pip install django`
- `.gitignore` : python, windows, macOS, django
- `django-admin startproject modelForm .`
- `django-admin startapp articles`
- `modelForm/settings.py` : `articles`앱 등록

## 01. 
### Modeling
- `articles/models.py`
```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 처음 게시물이 작성된 시간
    updated_at = models.DateTimeField(auto_now=True) # 수정된 시간, auto_now=True : 데이터가 저장되는 순간들을 계속해서 저장
```

### Migration
- `python manage.py makemigrations`
- `python manage.py migrate`