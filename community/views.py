from django.urls import reverse
from django.db.models import Q
from django.shortcuts import redirect
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Post, Comment, ScrabPost
from .serializers import PostSerializer, CommentSerializer, PostCreateSerializer, ScrabSerializer,PostListSerializer, ScrabListSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def post_create(request):
    if request.method == 'GET':
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostListSerializer(posts, many = True) # model의 Post 객체를 직렬화 함
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PostCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def my_post(request):
    kakao_id = request.query_params.get('kakao_id')
    posts = Post.objects.filter(kakao_id = kakao_id).order_by('-created_at')
    serializer = PostListSerializer(posts, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_post(request):
    post_id = request.data.get('post_id')
    kakao_id = request.data.get('kakao_id')

    try:
        posts = Post.objects.get(post_id = post_id, kakao_id = kakao_id)
        posts.comments.all().delete()
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def save_comment(request):
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_comment(request):
    post_id = request.data.get('post_id')
    comment_id = request.data.get('comment_id')

    try:
        comment = Comment.objects.get(post_id = post_id, comment_id = comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_scrab(request):
    post_id = request.query_params.get('post_id')
    kakao_id = request.query_params.get('kakao_id')

    try:
        scrab = ScrabPost.objects.get(post = post_id, kakao_id = kakao_id)
        scrab.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ScrabPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        try:
            post = self.get_object()  # post_id는 이미 get_object에서 처리됩니다.
            kakao_id = request.query_params.get('kakao_id')
            scrab_exists = ScrabPost.objects.filter(post_id=post, kakao_id=kakao_id).exists()
            serializer = self.get_serializer(post)
            data = serializer.data
            data['boolean_value'] = scrab_exists
 
            return Response(data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# class PostDetailView(generics.RetrieveAPIView): #제너릭 뷰는 DRF에서 자주 사용되는 API 패턴을 처리하는 추상화된 뷰 클래스입니다.
#     #RetrieveAPIView는 DRF의 제너릭 뷰 중 하나로, 단일 객체를 조회(read)하는 API 엔드포인트를 쉽게 만들 수 있도록 도와줍니다. 주어진 queryset에서 특정 객체를 조회하여 직렬화된 데이터를 반환하는 기능을 합니다. 이는 HTTP GET 요청을 처리하며, 기본적으로 retrieve 메서드를 사용하여 객체를 조회합니다.
#     queryset = Post.objects.all() #Post 모델의 모든 객체들을 반환함 Post 테이블을 전체를 반환한다고 생각하면 될듯

#     serializer_class = PostSerializer #여기에 post 정보는 물로 comment 정보까지 같이 들어가 있음

#     def get(self, request, *args, **kwargs):
#         # self: 매서드가 클래스 내부에 정의 -> 첫번쨰 파라미터는 항상 self임, 현재 클래스의 인스턴스를 참조한다. 이 get() 함수를 호출하는 클래스 인스턴스를 나타내고 있는 것이고, 함수는 그 클래스의 속성과 매서드에 접근이 가능하다. 
#         # request: 현재 http 요청 
#         # *args: 위치 인수임, 매서드 호출 시 위치로 전달된 추가적인 인수들을 포함, 주로 함수나 메서드에서 가변 개수의 인수를 받을 떄 사용한다. 
#         # **kwargs: 키워드 인수임, 매서드 호출 시 키워드로 전달된 추가적인 인수들을 포함한다. 주로 함수나 매서드에서 가변 개수의 키워드 인수를 받을 떄 사용한다. 
#         post_id = kwargs.get('pk') # pk는 url의 경로 변수 이름임, 'posts/<int:pk>/' 이 url 패턴에서 <int:pk> 부분이 url 경로애서 추출이 되어 뷰에 kwarg 사전으로 전달이 된다.
#         try:
#             post = self.get_object()
#             serializer = self.get_serializer(post) # REST framework 제네릭뷰에서 제공해주는 함수임 PostSerialize 클래스의 인스턴스를 생성해준다. 
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Post.DoesNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def scrab_post(request):
    serializer = ScrabSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

# @api_view(['GET'])
# def load_scrab(request):
#     scrab_posts = ScrabPost.objects.all().order_by('created_at')
#     serializer = ScrabSerializer(scrab_posts, many = True)
#     return Response(serializer.data)

@api_view(['GET'])
def load_scrab_list(request):
    kakao_id = request.query_params.get('kakao_id')
    if not kakao_id:
        return Response({'error': 'kakao_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    # ScrabPost 객체에서 kakao_id를 필터링하여 관련된 Post 객체를 가져옴
    scrab_posts = ScrabPost.objects.filter(kakao_id=kakao_id).order_by('created_at')
    post_ids = scrab_posts.values_list('post_id', flat=True)
    posts = Post.objects.filter(post_id__in=post_ids).order_by('-created_at')
    
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def redirect_scrab_detail(request, post_id):
    detail_url = reverse('post_detail', args = [post_id])
    return redirect(detail_url)

@api_view(['GET'])
def search_post(request):
    search_query = request.query_params.get('search_query')
    search_posts = Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    serializer = PostListSerializer(search_posts, many = True)
    return Response(serializer.data)

# @api_view(['POST'])
# def revise_post(request): 
#     kakao_id = request.query_params.get('kakao_id')
#     post_id = 
#     revise_content = request.query_params.get('revise_content')
#     revise_title = request.query_params.get('revise_title')
    