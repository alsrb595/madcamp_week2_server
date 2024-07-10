from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .models import User_Question
from .serializer import QuestionSerializer, QuestionListSerializer

@api_view(['GET', 'POST'])
def save_question(request):
    if request.method == 'POST':
        serializer = QuestionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        kakao_id = request.query_params.get('kakao_id')
        if kakao_id:
            questions = User_Question.objects.filter(kakao_id_id = kakao_id).order_by('question_id')
            serializer = QuestionSerializer(questions, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "kakao_id not provided"}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def detail_qustion(request):
#     questions