from authentication.serializers import MyTokenObtainPairSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from authentication.serializers import RegistrationSerializer
from rest_framework.generics import CreateAPIView


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: MyTokenObtainPairSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
