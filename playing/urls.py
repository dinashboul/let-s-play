from django.urls import path
from .views import PlayListView, PlayDetailView, PlayCreateView, PlayUpdateView, PlayDeleteView

urlpatterns = [
    path('play/', PlayListView.as_view(), name='play_list'),
    path('play/<int:pk>/', PlayDetailView.as_view(), name='play_detail'),
    path('play/create/', PlayCreateView.as_view(), name='play_create'),
    path('play/<int:pk>/update/', PlayUpdateView.as_view(), name='play_update'),
    path('play/<int:pk>/delete/', PlayDeleteView.as_view(), name='play_delete'),
]