from django.shortcuts import render
from rest_framework import generics
import models
# from serializers import *
# Create your views here.


def test():
    pass


class RecipeList(generics.ListAPIView):
    model = models.Recipe
    # serializer_class = RecipeSerializer
    queryset = models.Recipe.objects.all()

