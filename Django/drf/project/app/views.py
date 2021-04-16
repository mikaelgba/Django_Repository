from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import HQ
from .Serializers import HQSerializer

@csrf_exempt
def HQ_list(request):

    if( request.method == 'GET' ):

        hqs = HQ.objects.all()
        serializer = HQSerializer(hqs, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif( request.method == 'POST' ):

        data = JSONParser().parse(request)
        serializer = HQSerializer(data = data)

        if (serializer.is_valid()):
            
            serializer.save()
            return JsonResponse(serializer.data, status = 201)

        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def HQ_detail(request, pk):

    try:
        hq = HQ.objects.get(pk = pk)
    
    except(HQ.DoesNotExist):
        return Http.Response(status = 404)

    if( request.method == 'GET' ):

        serializer = HQSerializer(hq)
        return JsonResponse(serializer.data)

    elif( request.method == 'PUT' ):

        data = JSONParser().parse(request)
        serializer = HQSerializer(hq, data = data)

        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status = 400)

    elif( request.method == 'DELETE' ):
        hq.delete()
        return Http.Response(status = 204)