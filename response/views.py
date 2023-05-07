from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from .extras.word_explanation import explain 
from rest_framework.serializers import Serializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .extras.news import get_today_news
from rest_framework.response import Response
from .extras.gold import * 
# Create your views here.

class se(Serializer):
    key = serializers.CharField()

class SendRes(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = se
    def post(self,request):
        input_ = request.data['key']
        lang_ = request.data['lang']
        print('.........',input_,lang_)
        data = explain(input_,lang_)
        if data is None:
            data = {
                'key':input_,
                'value': "I am sorry i could't found the result. Please check spellings or try in another way(with new words)." 
            }
            return JsonResponse(data)
        return JsonResponse(data)
        

class GetNews(GenericAPIView):
    serializer_class = se
    queryset = User.objects.all()
    
    def post(self,request):
        type_ = request.data['type']
        data = get_today_news(type_)
        # new_data = []
        # for img , head , cont in zip(data['images'],data['headlines'],data['contents']):
        #     obj = {
        #         'img':img,
        #         'head':head,
        #         'cont':cont
        #     }
        #     new_data.append(obj)
        
        return Response(data)
    
class GetPrices(GenericAPIView):
    serializer_class = se
    queryset = User.objects.all()
    
    def get(self,request):
        
        data = {
            'gold':GOLD(),
            'BTC':'₹ '+BTC(),
            'GBP':'₹ '+GBP(),
            'EUR':'₹ '+EUR(),
            'USD':'₹ '+USD(),
            'AUD':'₹ '+AUD()
        }
      
        return Response(data)
    
    

