from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import HQ
from .Serializers import HQSerializer

# api-based classes
class HQ_list(APIView):

    def get (self, request):

        hqs = HQ.objects.all()
        serializer = HQSerializer(hqs, many=True)
        return Response(serializer.data)

    def post (self, request):

        serializer = HQSerializer(data = request.data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class HQ_details(APIView):
    
    def get_object(self, id):

        try:
            return HQ.objects.get(id = id)
    
        except(HQ.DoesNotExist):
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, id):

        hq = self.get_object(id)
        serializer = HQSerializer(hq)
        return Response(serializer.data)

    def put(self, request, id):

        hq = self.get_object(id)
        serializer = HQSerializer(hq, data = request.data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        hq = self.get_object(id)
        hq.delete()
        return Response(status = status.HTTP_NO_CONTENT)

# API generic view 
class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = HQSerializer
    queryset = HQ.objects.all()
    lookup_field = "id"
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)