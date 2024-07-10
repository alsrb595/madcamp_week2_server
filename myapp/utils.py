# import requests
# from datetime import datetime, timedelta
# from django.conf import settings
# from .models import UserToken

# def get_valid_access_token(user):
#     try:
#         user_token = UserToken.objects.get(user = user)
#     except UserToken.DoesNotExist:
#         return None
    
#     if user_token.is_access_token_expired():
#         if user_token.is_refresh_token_expired():
#             return None
        
#         token_api = 'https://kauth.kakao.com/oauth/token'
#         token_response = requests.post(
#             token_api,
#             data = {
#                 'grant_type': 'refresh_token',
#                 'client_id': settings.KAKAO_REST_API_KEY,
#                 'refresh_token': user_token.refresh_token
#             }
#         )

#         token_json = token_response.json()

#         if 'access_token' not in token_json:
#             return None 

#         token_json = token_response.json()
#         access_token = token_json.get('access_token')
#         expires_in = token_json.get('expires_in')
#         if expires_in is None:
#             return None
#         expires_at = datetime.utcnow() + timedelta(seconds = expires_in)

#         user_token.access_token = access_token
#         user_token.expires_at = expires_at
#         user_token.save()

#     return user_token.access_token