from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrViewOnly
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrViewOnly, IsAuthenticated]
    
    
    # def get_permissions(self, request, ):
    #     """Получение прав для действий."""
    #     if self.action == "create":
    #         return [IsAuthenticated()]
    #     elif self.action in ["update", "partial_update", "delete"]:
    #         return [IsAuthenticated(), IsOwnerOrViewOnly()]
    #     return []
    #
    