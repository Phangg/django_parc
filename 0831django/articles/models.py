from pyexpat import model
from random import random
from turtle import title
from venv import create
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
        # CharField -> 길이 제한이 있는 글 / max_length 필수 설정
    content = models.TextField()
        # TextField -> 글자수 많을 때 사용 / max_length ㄴㄴ 
        # 실제 저장 시, 길이에 대한 유효성 검증 X
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title