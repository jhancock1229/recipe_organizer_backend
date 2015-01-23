from rest_framework import serializers
from models import *


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Recipe

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        tags_data = validated_data.pop('tags')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients_data:
            try:
                ingredient = Ingredient.objects.get(name=ingredient["name"])
            except Ingredient.DoesNotExist:
                ingredient = Ingredient.objects.create(**ingredient)
            recipe.ingredients.add(ingredient)

        for tag in tags_data:
            try:
                tag = Tag.objects.get(name=tag["name"])
            except Tag.DoesNotExist:
                tag = Tag.objects.create(**tag)
            recipe.tags.add(tag)

        return recipe