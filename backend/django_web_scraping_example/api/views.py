from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NewsSerializer

from scraping.models import News
from django.http import JsonResponse

def NewsView(request):

    queryset = News.objects.all()
    data = list(queryset.values('newspaper','date','link','language','headline','sentiment'))
    return JsonResponse({
        'data':data
    })
