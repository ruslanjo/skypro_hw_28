from django.urls import path

from ads.views import CategoryView, CategoriesView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView

urlpatterns = [
    path('', CategoriesView.as_view()),
    path('<int:pk>/delete/', CategoryDeleteView.as_view()),
    path('<int:pk>/update/', CategoryUpdateView.as_view()),
    path('<int:pk>/', CategoryView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    ]
