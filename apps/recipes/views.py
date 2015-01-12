from django.shortcuts import render
from rest_framework import generics
from models import *
from serializers import *


def test():
    pass


class RecipeList(generics.ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

