from rest_framework import serializers
from .models import User

# 프론트로부터 받은 json 데이터를 파이썬 객체로 변환하기 위한 코드
class UserSerializer(serializers.ModelSerializer): #UserSerializer는 User 모델의 필드와 검증을 자동으로 가져옴
    class Meta:
        model = User #어떤 모델 클래스를 기반으로 하는지
        fields = '__all__' #어떤 필드를 포함할지 또는 제외할지를 정해주는 것
'''
직렬화(Serialization): KakaoUser 모델 인스턴스를 JSON 데이터로 변환합니다. serializer.data를 통해 모델 데이터를 JSON 형식으로 접근할 수 있습니다.
역직렬화(Deserialization): JSON 데이터를 KakaoUser 모델 인스턴스로 변환합니다. serializer.is_valid() 메서드를 호출하여 데이터의 유효성을 검사하고, serializer.save() 메서드를 통해 데이터베이스에 저장합니다.
'''