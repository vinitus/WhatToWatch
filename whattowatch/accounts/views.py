from accounts.models import User
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.http import JsonResponse
import requests
from rest_framework import status
from json.decoder import JSONDecodeError
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response


KAKAO_CALLBACK_URI = "http://localhost:8000/accounts/kakao/callback/"
BASE_URL = ''

@api_view(['POST'])
def kakao_login(request):
    kakao = request.data
    kakao_id = request.data['id']
    kakao_nickname = request.data['kakao_account']['profile']['nickname']
    kakao_email = request.data['kakao_account']['email']

    return Response({'fuck':1})

class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = KAKAO_CALLBACK_URI