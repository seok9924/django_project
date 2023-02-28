# from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic import ListView,CreateView,DetailView,DeleteView


# def index(request):
#     posts=Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/index.html',{
#             'posts' :posts
#                          },
#     )

# fbv 로 만든 인덱스
# def single_post_page(request,pk) :
#     post=Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
#     )
class PostList(ListView):
    model = Post
    ordering = '-pk'

#     template_name = 'blog/index.html'
# 장고가 제공하는 ListView 는 모델명 뒤에 _list가 붙은 html 파일을 기본 템플릿으로 사용
# html 내에서도 post_list로 받음



class PostDetail(DetailView):
    model=Post