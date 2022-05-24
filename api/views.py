from django.shortcuts import render
from rest_framework import views,status
from rest_framework.response import Response
from .models import myModel
from .serializers import myModelSerializer

# Create your views here.

class RetrieveView(views.APIView):

    def get(self,request):
        mymodels = myModel.objects.all()
        serializer = myModelSerializer(mymodels,many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)


class CreateView(views.APIView):

    def post(self,request):
        data = request.data
        serializer = myModelSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            mymodel = serializer.save()
            serializer = myModelSerializer(mymodel)
            print(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({"errors":serializer.errors})        


        







