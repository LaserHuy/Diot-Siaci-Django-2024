from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello, World!')
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'main/post_list.html', {'posts': posts})