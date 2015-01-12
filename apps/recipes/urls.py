from django.conf.urls import patterns, include, url
from views import *
urlpatterns = patterns(
    '',

    url(r'^recipes/$', RecipeList.as_view(), name='recipe-list'),

)