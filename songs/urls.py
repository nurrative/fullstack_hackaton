from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from .views import *

router = DefaultRouter()
router.register('albums', AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('songs/', SongListView.as_view()),
    path('songs/upload/', SongUploadView.as_view()),
    path('songs/<int:pk>/', SongRetrieveUpdateDestroyView.as_view()),
    path('artists/', ArtistListCreateAPIView.as_view()),
    path('songs/artist/<int:id>/', ArtistDetailView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)