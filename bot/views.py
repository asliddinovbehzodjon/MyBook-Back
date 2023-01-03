from django.shortcuts import render

# Create your views here.
from .serializer import BotSerializer
from .models import BotUsers
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from books.filter import BotFilter
from django_filters.rest_framework import DjangoFilterBackend
class BotViewset(ModelViewSet):
    queryset =  BotUsers.objects.all()
    serializer_class = BotSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_class = BotFilter
    search_fields = ('t_id',)
class ChangeLang(APIView):
    def get(self,request,t_id,language):
        user = BotUsers.objects.get(t_id=t_id)
        user.language = language
        user.save()
        return Response(data={'status':'Language updated'})
        
