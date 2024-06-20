from django.shortcuts import render, redirect
from .models import NewsArticle, Category
from .forms import NewsArticleForm


def news_list(request):
    form = NewsArticleForm()
    if request.method == "POST":
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("news_list")
    else:
        form = NewsArticleForm()

    category_id = request.GET.get("category")
    if category_id:
        articles = NewsArticle.objects.filter(category_id=category_id).order_by("-date")
    else:
        articles = NewsArticle.objects.all().order_by("-date")
    categories = Category.objects.all()

    return render(
        request,
        "news/news_list.html",
        {"articles": articles, "categories": categories, "form": form},
    )
