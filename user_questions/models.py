from django.db import models
from myapp.models import User
# Create your models here.

class User_Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    kakao_id = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    answer = models.TextField()

    def get_summary(self):
        return self.content[:30]