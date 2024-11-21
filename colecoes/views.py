from rest_framework import generics, permissions
from .models import Colecao
from .serializers import ColecaoSerializer

class ColecaoListCreateView(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(colecionador=self.request.user)

class ColecaoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [permissions.IsAuthenticated]
