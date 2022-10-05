from django.urls import path

from ads.views import AdsView, AdView, AdCreateView, AdUpdateView, AdDeleteView, AdUploadImageView

urlpatterns = [
    path('', AdsView.as_view()),
    path('<int:pk>/', AdView.as_view()),
    path('ads/create/', AdCreateView.as_view()),
    path('ads/<int:pk>/update/', AdUpdateView.as_view()),
    path('ads/<int:pk>/delete/', AdDeleteView.as_view()),
    path('ads/<int:pk>/upload_image/', AdUploadImageView.as_view()),
]
