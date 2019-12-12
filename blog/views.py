from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from blog.models import Post


def post_list(request):
    # print('h:', HttpResponse(post_list))
    # Templates 을 찾을 경로에서 post_list.html 찾아 그 파일을 text 로 만들어서 HttpResponse 형태로 동작한다
    # 위 기능을 하는 shortcut 함수

    # content = loader.render_to_string('post_list.html', None, request)
    # return HttpResponse(content)

    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)


def post_detail(request):
    post = Post.objects.all()[0]
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)