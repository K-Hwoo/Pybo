from django.db import models

# Create your models here.

class Question(models.Model) :
    subject = models.CharField(max_length=200)
    # 글자수의 길이가 제한된 텍스트는 CharField를 사용
    content = models.TextField()
    # 글자수를 제한할 수 없는 텍스트는 TextField를 사용
    create_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.subject
    
class Answer(models.Model) :
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    

    
