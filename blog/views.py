from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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


def post_detail(request, pk):
    # print('request:', request)
    # posts = Post.objects.filter(pk=pk)
    # post = posts[0]
    # try:
    #     post = Post.objects.filter(pk=pk)
    # except Post.DoesNotExist:
    #     return HttpResponse('없음!!')
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)


def post_add(request):
    return render(request, 'post_add.html')
