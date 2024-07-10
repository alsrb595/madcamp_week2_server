from django.shortcuts import redirect, render
from django.views import View
from django.conf import settings
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializer import UserSerializer

@api_view(['POST'])
def save_user(request):
    kakao_id = request.data.get('id')
    nickname = request.data.get('nickname')
    profile_image = request.data.get('profile_image')
    thumbnail_image = request.data.get('thumbnail_image')

    try:
        user = User.objects.get(kakao_id = kakao_id) 
        # User는 장고 모델 클래스임, User는 데이터베이스의 테이블과 매핑되어 있다
        #objects: 장고의 모델 메니저임, 데이터베이스 쿼리를 수행하는 여러 메소드 제공해줌
        #get(): 주어진 조건에 맞는 단일 레코드를 데이터베이스에서 가져옴, 조건에 맞는 레코드가 없거나 여러 개의 레코드가 있는 경우 예외를 발생시킴
        #kakao_id = kakao_id: 하나는 User 모델의 필드임, 하나는 함수의 인자로 전달된 값임 즉, 필드 값과 주어진 값이 일치하는 레코드를 찾음
        serializer = UserSerializer(user)
        return Response(status=status.HTTP_200_OK)
    
    except User.DoesNotExist:
        serializer = UserSerializer(data = request.data)
    
        if serializer.is_valid(): # serializer.is_valid() 메서드는 시리얼라이저에 전달된 데이터가 모든 필드와 검증 조건을 만족하는지 검사
            serializer.save()
            #serializer.save() 메서드를 호출하면 시리얼라이저에 전달된 데이터가 검증된 후 
            # 해당 모델 인스턴스로 저장됩니다. 이 과정에서 시리얼라이저는 내부적으로 모델의 save() 메서드를 호출하여 데이터베이스에 객체를 저장
            return Response(status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delete_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')

    try:
        user = User.objects.get(kakao_id = user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



































# from .utils import get_valid_access_token

# class KakaoSignInView(View):
#     def get(self, request):
#         app_key = settings.KAKAO_REST_API_KEY
#         redirect_uri = 'http://143.248.226.32:8000/users/signin/kakao/callback/'
#         kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'
#         return redirect(
#             f'{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}'
#         )
 
# class KakaoSignInCallBackView(View):
#     def get(self, request):
#         code = request.GET.get('code') #이 부분이 인가 코드가 되는 것
#         redirect_uri = 'http://143.248.226.32:8000/users/signin/kakao/callback/'
#         token_api = 'https://kauth.kakao.com/oauth/token'
#         client_id = settings.KAKAO_REST_API_KEY
#         token_response = requests.post(
#             token_api,
#             data={
#                 'grant_type': 'authorization_code',
#                 'client_id': client_id,
#                 'redirect_uri': redirect_uri,
#                 'code': code,
#             }
#         )

#         token_json = token_response.json()
#         print("Token Response JSON:", token_json)
#         access_token = token_json.get('access_token')
#         refresh_token = token_json.get('refresh_token')
#         expires_in = token_json.get('expires_in')

#         expires_at = datetime.utcnow() + timedelta(seconds = 30)
#         refresh_expires_in = 60 * 60 * 24* 30
#         refresh_expires_at = datetime.utcnow() + timedelta(seconds=refresh_expires_in)


#         user_info_response = requests.get(
#             'https://kapi.kakao.com/v2/user/me',
#             headers={'Authorization': f'Bearer {access_token}'}
#         )

#         user_info = user_info_response.json()
#         print("user info: ", user_info)

#         kakao_id = user_info['id']
#         nickname = user_info.get('properties', {}).get('nickname', '')
#         profile_image = user_info['properties']['profile_image']
#         thumbnail_image = user_info['properties']['thumbnail_image']

#         user, created = User.objects.get_or_create(
#             kakao_id = kakao_id,
#             defaults={
#                 'nickname': nickname,
#                 'profile_image': profile_image,
#                 'thumbnail_image': thumbnail_image
#             }
#         )

#         if not created:
#             user.nickname = nickname
#             user.profile_image = profile_image
#             user.thumbnail_image = thumbnail_image
#             user.save()

        
#         # UserToken.objects.update_or_create(
#         #     user = user,
#         #     defaults={
#         #         'access_token': access_token,
#         #         'refresh_token': refresh_token,
#         #         'expires_at': expires_at,
#         #         'refresh_expires_at': refresh_expires_at,
#         #     }
#         # )

        
#         return render(request, 'callback.html', {'user_info': user_info})


# class UserProfileView(View):
#     def get(self, request):
#         user = request.user
#         return render(request, 'profile.html', {'user': user})
    

# class UserProfileView(View):
#     def get(self, request):
#         user = request.user
#         access_token = get_valid_access_token(user)
#         if not access_token:
#             return redirect('kakao_singin')
        
#         user_info_response = requests.get(
#             'https://kapi.kakao.com/v2/user/me',
#             headers={'Authorization': f'Bearer {access_token}'}

#         )

#         user_info = user_info_response.json()
#         return render(request, 'profile.html', {'user_info': user_info})