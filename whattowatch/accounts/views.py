from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.conf import settings
from . import models

class SignupView(APIView):
    def post(self, request):
        User = settings.AUTH_USER_MODEL
        user = User.objects.create_user(username=request.data['id'], password=request.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key})