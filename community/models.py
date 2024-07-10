from django.db import models


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)  # 자동 증가 필드, 주 키로 설정됨
    kakao_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post_picture = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.title

    def get_summary(self):
        return self.content[:30]

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)  # 자동 증가 필드, 주 키로 설정됨
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add=True로 변경
    kakao_id = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f'Comment {self.kakao_id} on {self.post.title}'

class ScrabPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='scrabs')
    kakao_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add=True로 변경
    post_picture = models.ImageField(upload_to='images/', blank=True, null=True,)
