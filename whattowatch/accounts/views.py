from accounts.models import User
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from django.http import JsonResponse
import requests
from json.decoder import JSONDecodeError
from django.shortcuts import redirect

'http://127.0.0.1:8000/accounts/kakao/callback/'
BASE_URL = 'http://127.0.0.1:8000/'
KAKAO_CALLBACK_URI = BASE_URL + 'accounts/kakao/callback/'
client_id = '9e23cba329b4a051b6a8d2fa14e8ddf2'

def kakao_login(request):
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code&scope=account_email")
    # res = requests.get(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code&scope=account_email")
    # tmp = requests.get(res.url)
    # print(res.text)
    # print(tmp.text)
    # return redirect()

def kakao_callback(request):
    code = request.GET.get("code")
    print(code)
    token_request = requests.get(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={KAKAO_CALLBACK_URI}&code={code}")
    token_response_json = token_request.json()
    error = token_response_json.get("error", None)
    if error is not None:
        raise JSONDecodeError(error)

    access_token = token_response_json.get("access_token")

    profile_request = requests.post(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    profile_json = profile_request.json()

    kakao_account = profile_json.get("kakao_account")
    email = kakao_account.get("email", None)

    try:
        user = User.objects.get(email=email)

        data = {'access_token': access_token, 'code': code}
        accept = requests.post(f"{BASE_URL}accounts/kakao/login/finish/", data=data)

        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)

    except User.DoesNotExist:
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(f"{BASE_URL}accounts/kakao/login/finish/", data=data)

        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)

class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter