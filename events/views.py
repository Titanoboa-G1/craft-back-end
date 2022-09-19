from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import datetime
from .models import Event
from rest_framework import viewsets
from rest_framework import generics
from .serializers import EventSerializer , userEventSerializer
from utils.permissions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from account.models import *
class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = (IsOwnerUserOrReadOnly,IsAuthenticated,)



class UpcomingEventsList(generics.ListCreateAPIView):
    serializer_class = EventSerializer()

    # def get_serializer_context(self,request):
    #     user = decode_token(request.headers.get('Authorization'))
    #     context = super().get_serializer_context()
    #
    #     context["user"] = user
    #     return context

    # def get_queryset(self):
    #     today = datetime.datetime.today()
    #     return Event.objects.filter(day__gte=today)
    queryset = Event.objects.all()
    serializer_class= userEventSerializer
    permission_classes = (IsAdminORReadOnly,IsAuthenticated)
    def post(self,request):
        user=decode_token(request.headers.get('Authorization'))
        # print("hello")
        # print(user)
        EventSerializer(user)
        if CustomUser.objects.filter(pk=user)[0].is_staff:
            print(CustomUser.objects.filter(pk=user)[0].email)
            self.serializer_class= EventSerializer
        else :
            print(CustomUser.objects.filter(pk=user)[0].role)
        return Response({},status=status.HTTP_201_CREATED)



import jwt
from django.conf import settings
def decode_token(token):
    try:
        print(token)
        payload = jwt.decode(token.split(" ")[1], "eh-u^@&mby4ug_020@m3*j%pg+h)5-!1^xf%x!gbo3vlp-h2", algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'