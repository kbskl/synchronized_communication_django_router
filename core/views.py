from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from util.route_manager import RouteManager


class SubscribeAPI(APIView):

    def get(self, request, format=None):
        RouteManager().subscribe()
        return Response("SubscribeAPI", status=status.HTTP_200_OK)
