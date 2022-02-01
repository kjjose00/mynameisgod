from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    # authentication_classes=[SessionAuthentication] #local declaration
    # # permission_classes=[IsAdminUser]
    permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
