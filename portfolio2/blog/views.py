from django.shortcuts import render
from .models import Posts,Project
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def index(request):
     list1 = Project.objects.order_by('-Date')[:7]
     if list1.exists():
          context =  list1;
     return render(request,'blog/home.html',{'list':list1})

def articles(request):
     post_list =Posts.objects.all()
     page = request.GET.get('page',1)

     paginator = Paginator(post_list,3)
     try:
          posts = paginator.page(page)
     except PageNotAnInteger:
          posts = paginator.page(1)
     except EmptyPage:
          posts = paginator.page(paginator.num_pages)
     return render(request,'blog/index.html',{'posts':posts})

def blog_expand(request,pk):
     req = Posts.objects.get(pk=pk)
     context={'s_post':req}
     return render(request,'blog/project_detail.html', context)

def about_page(request):
     return render(request,'blog/about.html')