from django.urls import path
from api.views import GetBidsView, LogBidView, BidDeleteView

urlpatterns = [
    path('', LogBidView.as_view(), name="log_bids"),
    path('check/', GetBidsView.as_view(), name="get_bids"),
    path('check/<int:id>/', BidDeleteView.as_view(), name="delete_bid"),
]