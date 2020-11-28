from django.urls import path
from blog.views import BlogView, detailViewPost, CategoriesView


urlpatterns = [
    path('', BlogView.as_view()),
    path("<str:url>/", CategoriesView.as_view(), name="category_url"),
    path("<str:category_url>/<slug:url>/", detailViewPost),
]
