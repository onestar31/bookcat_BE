from django.shortcuts import render
#from .models import Review, User   # serializers를 통해 DB를 받았기 때문에 models import 불필요
#from user.models import User
from datetime import date

from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class ReviewView(APIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request):
        data = request.data
        r : Review = Review (
            bookId = data.get('bid'),
            userId = User.objects.get(id=data.get('uid')),
            reviewTitle = data.get('rtitle'),
            reviewDate = date.today(),
            reviewRate = data.get('rate'),
            reviewTxt = data.get('rtext')
        )
        r.save()
        return Response({'message':'서평 등록이 완료되었습니다.'}, status=status.HTTP_200_OK)

    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            review_qr_serializer = ReviewSerializer(Review.objects.all(), many=True)
            return Response(review_qr_serializer.data, status=status.HTTP_200_OK)
        else:
            rid = kwargs.get('id')
            review_serializer = ReviewSerializer(Review.objects.get(id=rid))
            return Response(review_serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        rid = data.get('rid')
        review = Review.objects.get(id=rid)
        review.reviewTitle = data.get('rtitle')
        review.reviewRate = data.get('rate')
        review.reviewTxt = data.get('rtext')
        review.save()
        return Response({'message':'서평 수정이 완료되었습니다.'}, status=status.HTTP_200_OK)

    def delete(self, request):
        data = request.data
        rid = data.get('reviewId')
        review = Review.objects.get(id=rid)
        review.delete()
        return Response({'message':'서평 삭제가 완료되었습니다.'}, status=status.HTTP_200_OK)

def index(request):
    return render(request, 'index.html')