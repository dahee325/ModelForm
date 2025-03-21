from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def create(request):
    # new/ => 빈 종이를 보여주는 기능
    # create/ => 사용자가 입력한 데이터 저장
    # -------------------------------------
    # GET create/ => 빈 종이를 보여주는 기능
    # POST create/ => 사용자가 입력한 데이터 저장
    # => create/로 합쳐짐

    if request.method == 'POST':
        form = ArticleForm(request.POST) # request.POST의 딕셔너리 값을 html으로 바꿔줌

        if form.is_valid(): # validation : form에 있는 데이터가 유효한가요?
            form.save() # 있다면 저장
            return redirect('articles:index')

    else: # 먼저 실행됨
        form = ArticleForm()

    # else일 경우 항상 실행
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)