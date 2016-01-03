from django.shortcuts import render, render_to_response, get_object_or_404
from Home.models import Post, Comment


def front(request):
    return render(request, 'home/front.html')


def blog(request):
    return render_to_response('home/blog.html', {
        'posts': Post.objects.order_by('-creation_date')
    })


def contact(request):
    return render(request, 'home/contact.html')


def page(request, slug):
    if request.method == 'POST':
        username = request.POST.get('username')
        body = request.POST.get('body')
        post = Post.objects.get(pk=1)
        new_comment = Comment.objects.create(post_at=post, submitter=username, text=body)
        new_comment.save()
    comments = Comment.objects.all()
    return render_to_response('home/post.html', {
        'post': get_object_or_404(Post, slug=slug),
        'comments': comments
    })

