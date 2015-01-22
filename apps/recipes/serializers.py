from rest_framework import serializers
from models import *


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('name', 'description', 'directions', 'ingredients')

    def create(self, validated_data):
        # ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        # for ingredient_data in ingredients_data:
        #     Ingredient.objects.create(**ingredient_data)
        return recipe


class NestedRecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe