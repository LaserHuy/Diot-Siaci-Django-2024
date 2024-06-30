from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import translation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings  # Add this line
from .serializers import *
from .models import *

# Create your views here.


def home(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return render(request, 'home.html', {'posts': serializer.data})


def set_language(request):
    user_language = request.GET.get('language', 'en')
    translation.activate(user_language)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response