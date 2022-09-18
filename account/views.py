from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny

from account.serializers import UserSerializer
from utils.permissions import IsOwnerUserOrReadOnly


class UserListCreateView(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerUserOrReadOnly,)