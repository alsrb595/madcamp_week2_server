from rest_framework import serializers
from .models import Post, Comment, ScrabPost
from myapp.models import User

'''
직렬화는 Django REST framework에서 모델 인스턴스를 JSON, XML 등의 형식으로 변환하여 데이터를 전송하거나 저장할 수 있도록 하는 중요한 과정입니다. 
이를 통해 클라이언트와 서버 간의 데이터 전송, 데이터 검증, 일관된 데이터 표현 등을 효율적으로 처리할 수 있습니다. 직렬화는 API 개발의 핵심적인 부분으로, 
데이터의 변환과 검증을 담당
'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['kakao_id', 'comment_id', 'post', 'created_at', 'content', 'user']
    
    def get_user(self, obj):
        try:
            user = User.objects.get(kakao_id=obj.kakao_id)
            return UserSerializer(user).data
        except User.DoesNotExist:
            return None

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only = True)
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['post_id', 'title', 'kakao_id', 'content', 'post_picture', 'created_at', 'comments', 'user']
    def get_user(self, obj):
        try:
            user = User.objects.get(kakao_id=obj.kakao_id)
            return UserSerializer(user).data
        except User.DoesNotExist:
            return None
    

class ScrabSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many = True, read_only = True)
    class Meta:
        model = ScrabPost
        fields = ['post', 'kakao_id', 'created_at']

class PostListSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(source = 'comments.count',read_only = True)
    # comments: model의 related_name을 의미한다. Django에서 기본적으로 역참조되는 관계에 대해 생성되는 RelatedManager입니다. 예를 들어, Post 모델이 여러 개의 Comment 모델과 연결되어 있다면, Post 인스턴스는 comment_set을 통해 해당 댓글들에 접근할 수 있습니다.
    # count: 관련된 Comment 객체의 수를 반환한다. 

    summary = serializers.SerializerMethodField() # summery 필드를 정의하는 것임, 

    class Meta:
        model = Post
        fields = ['post_id', 'title', 'kakao_id', 'created_at', 'summary', 'post_picture', 'comments_count']

    def get_summary(self, obj): #매서드를 정의하는, get_<field_name> 형식의 메서드를 정의함. 여기서 <field_name>은 SerializerMethodField로 정의한 필드의 이름임
        # 직렬화 과정에서 model 안에 있는 def get_summery(self)를 통해 반환된 값이 summery에 할당이 됨
        return obj.get_summary()
    
class ScrabListSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField(source = 'post.post_id', read_only = True) # source 부분의 post의 의미는 ScrabPost 모델의 foreignkey 필드인 post를 의미 함, source를 통해 관계를 참조함
    title = serializers.CharField(source = 'post.title', read_only = True)
    summary = serializers.SerializerMethodField()
    post_picture = serializers.ImageField(source = 'post.post_picture', read_only = True)
    post_kakao_id = serializers.CharField(source = 'post.kakao_id', read_only = True)
    scrab_kakao_id = serializers.CharField(read_only = True)
    
    class Meta:
        model = ScrabPost
        fields = ['post_id', 'title', 'summary', 'post_picture', 'post_kakao_id', 'scrab_kakao_id', 'created_at', 'comments']

    def get_summary(self, obj):
        return obj.post.get_summary()