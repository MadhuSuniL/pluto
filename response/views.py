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
import random, time
from sources.checks import GetRes
from sources.name_patterns import sorry
# Create your views here.

class se(Serializer):
    key = serializers.CharField()

class SendRes(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = se
    def post(self,request):
        input_ = request.data['key']
        lang_ = request.data.get('lang','en')
        print('.........',input_,lang_)
        data = GetRes(input_.strip(),lang_)

        if data is None:
            data = {
                    'id':str(time.time()),
                    'key':input_,
                    'img':'none',
                    'value':random.choice(sorry),
                    'copy':'',
                    'extra':['sample'+str(x) for x in range(1,6)],
                }
            return JsonResponse(data,safe=False)        
        
        return JsonResponse(data,safe=False)
        

# class GetNews(GenericAPIView):
#     serializer_class = se
#     queryset = User.objects.all()
    
#     def post(self,request):
#         type_ = request.data['type']
#         data = get_today_news(type_)
#         # new_data = []
#         # for img , head , cont in zip(data['images'],data['headlines'],data['contents']):
#         #     obj = {
#         #         'img':img,
#         #         'head':head,
#         #         'cont':cont
#         #     }
#         #     new_data.append(obj)
        
#         return Response(data)
    
# class GetPrices(GenericAPIView):
#     serializer_class = se
#     queryset = User.objects.all()
    
#     def get(self,request):
        
#         data = {
#             'gold':GOLD(),
#             'BTC':'₹ '+BTC(),
#             'GBP':'₹ '+GBP(),
#             'EUR':'₹ '+EUR(),
#             'USD':'₹ '+USD(),
#             'AUD':'₹ '+AUD()
#         }
      
#         return Response(data)
    
    

