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

### admin에 Article추가
- `articles/admin.py`
```python
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
```

### superuser 등록
- `python manage.py createsuperuser` : admin, , 1234, 1234, y

### 공통 base.html 설정
- 폴더의 최상단(`modelform/`)에 `templates`파일 생성 => `modelForm/settings.py`에 등록
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        ...
    },
]
```
- `modelsform/templastes`폴더에 `base.html`파일 생성
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>여기는 base</h1>
    {% block body %}

    {% endblock %}
</body>
</html>
```