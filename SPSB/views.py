from django.shortcuts import render, redirect
from .models import NewsPost, Category, Media, NewsPostMedia
from .forms import NewsPostForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def news(request):
    # news_posts = NewsPost.objects.prefetch_related('mediapost_set__media').all().order_by('-created_at')
    # news_posts = NewsPost.objects.prefetch_related('post_media__media').all()
    news_posts = NewsPost.objects.prefetch_related('post_media__media').all().order_by('-created_at')

    return render(request, 'news.html', {
        'news_posts': news_posts
    })

def edit_post(request, id):
    post = NewsPost.objects.get(id=id)

    if request.method == 'POST':
        form = NewsPostForm(request.POST, instance=post)

        if form.is_valid():
            form.save(user=request.user)
            return redirect('news')
    else:
        form = NewsPostForm(instance=post)

    return render(request, 'edit_post.html', {
        'form': form,
        'post': post
    })

def delete_post(request, id):
    post = NewsPost.objects.get(id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('news')

    return render(request, 'delete_post.html', {
        'post': post
    })