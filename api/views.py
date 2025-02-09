from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Bid
from api.serializers import BidSerializer
from datetime import datetime

class LogBidView(APIView):
    serializer_class = BidSerializer

    def post(self, request):
        required_fields = ['position', 'company', 'link', 'resume']
        data = {field: request.data.get(field) for field in required_fields}

        if None in data.values():
            return Response({'error': 'All fields are required'}, status=400)
        
        data['created_at'] = datetime.now()
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


class GetBidsView(APIView):
    def post(self, request):
        position = request.data.get('position')
        company = request.data.get('company')

        if not position or not company:
            return Response({'error': 'Company and Position are required'}, status=400)
        
        bids = Bid.objects.filter(company=company, position=position)
        if not bids.exists():
            return Response({'error': 'No bids found for the given company and position'}, status=404)
        
        serializer = BidSerializer(bids, many=True)
        return Response(serializer.data, status=200)

    def get(self, request):
        bids = Bid.objects.all()
        serializer = BidSerializer(bids, many=True)
        return Response(serializer.data, status=200)

class BidDeleteView(APIView):
    def delete(self, request, id):
        try:
            bid = Bid.objects.get(id=id)
        except Bid.DoesNotExist:
            return Response({'error': 'Entry not found'}, status=404)
        
        bid.delete()
        
        return Response(status=200)
