from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Country
from .serializers import CountrySerializer

class BasicAuthView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        content = {
            'Data': "Validation succesfull for Basic Authentication",
            'user': str(request.user),
        }
        return Response(content)

class TokenExampleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        content = {
            'Data': "Validation succesfull for Token Authentication",
            'user': str(request.user),
        }
        return Response(content)

class JwtExampleView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        content = {
            'Data': "Validation succesfull for JWT token.",
            'user': str(request.user),
        }
        return Response(content)

@api_view(['POST','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def country(request):
    """API business logic handling."""
    try:
        if request.method == "POST":
            api_data = JSONParser().parse(request)
            country_data = CountrySerializer(data=api_data)
            if country_data.is_valid():
                country_data.save()
                return JsonResponse(country_data.data, status=status.HTTP_201_CREATED)
            return JsonResponse(country_data.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == "GET":
            country_list = Country.objects.all()
            country_list = CountrySerializer(country_list, many=True)
            return JsonResponse(country_list.data, safe=False)

    except Exception as exc:
        return JsonResponse({"error":str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
