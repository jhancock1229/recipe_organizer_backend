from django.shortcuts import render
from rest_framework import generics
from serializers import *


class RecipeList(generics.ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class IngredientList(generics.ListAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()