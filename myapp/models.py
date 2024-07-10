from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime, timedelta

# Create your models here.
class User(models.Model):
    kakao_id = models.CharField(max_length = 255, primary_key=True)
    nickname = models.CharField(max_length = 255)
    profile_image = models.URLField(max_length=255, blank=True, null=True)
    thumbnail_image = models.URLField(max_length=255, blank = True, null = True)
    def __str__(self):
        return self.nickname #예를 들어, KakaoUser 모델에 __str__ 메서드를 정의하면, 해당 객체를 문자열로 표현할 때 nickname 필드의 값을 반환하도록 할 수 있습니다. 







# class UserManager(BaseUserManager):
#     def create_user(self, nickname, kakao_id, profile_image = None, thumbnail_image = None, password = None):
#         if not kakao_id:
#             raise ValueError("Users must have an email address")
#         user = self.model(
#             nickname = nickname,
#             kakao_id = kakao_id,
#             profile_image = profile_image,
#             thumbnail_image = thumbnail_image,
#         )
#         user.save(using = self._db)
#         return user

# class User(AbstractBaseUser):
#     kakao_id = models.CharField(max_length=30, nunique=True)
#     nickname = models.CharField(max_length=30)
#     profile_image = models.URLField(max_length=255, blank=True, null=True)
#     thumbnail_image = models.URLField(max_length=255, blank = True, null = True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'kakao_id'
#     REQUIRED_FIELDS = ['nickname']

#     def __str__(self):
#         return self.nickname
    
#     def has_perm(self, perm, obj = None):
#         return True
    
#     def has_module_parms(self, app_label):
#         return True
    
#     def is_stadd(self):
#         return self.is_admin


# class UserToken(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     access_token = models.CharField(max_length=255)
#     refresh_token = models.CharField(max_length=255)
#     expires_at = models.DateTimeField() # 엑세스 토큰 만료 시간
#     refresh_expire_at = models.DateTimeField() #리프레시 토큰 만료 시간
    

#     def is_access_token_expired(self):
#         return datetime.utcnow() >= self.expires_at
    
#     def is_refresh_token_expired(self):
#         return datetime.utcnow() >= self.refresh_expire_at