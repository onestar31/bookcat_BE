from django.db import models
from user.models import User

class Review(models.Model):
    # reviewId(PK)는 자동 id 사용
    bookId = models.CharField(max_length=30)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewTitle = models.CharField(max_length=200)
    reviewDate = models.DateField(auto_now_add=True)
    reviewRate = models.IntegerField()
    reviewTxt = models.TextField()

    def __int__(self):
        return self.reviewTitle