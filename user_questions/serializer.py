from .models import User_Question
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Question
        fields = '__all__'

class QuestionListSerializer(serializers.ModelSerializer):
    summary = serializers.SerializerMethodField()

    class Meta:
        model = User_Question
        fields = ['question_id', 'kakao_id', 'summary']