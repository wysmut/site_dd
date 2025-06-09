from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Result

class ResultsData(APIView):
    def get(self, request):
        user_id = request.GET.get('user_id')
        if not user_id:
            return Response({"error": "user_id required"}, status=status.HTTP_400_BAD_REQUEST)
        
        results = Result.objects.filter(user_id=user_id).values('test__title', 'score', 'date_taken')
        return Response(list(results))
