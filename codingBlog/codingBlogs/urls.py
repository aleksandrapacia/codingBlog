"""Defines URL addresses' patterns for codingBlogs (app)"""

from django.urls import path
# url() -> map URL on views
from . import views # import views from the same folder as views module -> (.)
app_name = 'codingBlog'
urlpatterns = [
    path('', view.index, name='index'),
]