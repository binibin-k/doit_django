from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author: 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.title}'
    
    def get_absolute_url(self): # 모델의 레코드별 URL 생성 규칙을 정의
        return f'/blog/{self.pk}' # 각 레코드의 pk값이 넘어온다
        