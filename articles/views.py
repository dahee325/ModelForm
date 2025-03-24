from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

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


def detail(request, id):
    article = Article.objects.get(id=id)
    comments = article.comment_set.all()
    form = CommentForm()

    context = {
        'article': article,
        'form': form,
        'comments': comments,
    }
    return render(request, 'detail.html', context)


def update(request, id):
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=id)
    
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }

    return render(request, 'update.html', context)


def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')


def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            article = Article.objects.get(id=article_id)
            comment.article = article
            comment.save()

            return redirect('articles:detail', id=article_id)

    else:
        return redirect('articles:index')


def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('articles:detail', id=article_id)