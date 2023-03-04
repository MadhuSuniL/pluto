from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from .extras.word_explanation import explain 
from rest_framework.serializers import Serializer
from rest_framework import serializers
from django.contrib.auth.models import User
# Create your views here.

class se(Serializer):
    key = serializers.CharField()

class SendRes(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = se
    def post(self,request):
        input_ = request.data['key']
        data = explain(input_)
        if data is None:
            data = {
                'key':input_,
                'value': "I am sorry i could't found the result. Please check spellings or try in another way(with new words)." 
            }
            return JsonResponse(data)
        return JsonResponse(data)
        

