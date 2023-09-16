
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status as http_status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from stractor.common.models import Symptom
from stractor.common.serializers.serializers import SymptomSerializer


class SymptomViewSet(ListModelMixin, GenericViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

    @swagger_auto_schema(
        tags=["symptom"],
        operation_id="symptom list",
        responses={200: SymptomSerializer(many=True)})
    @action(
        methods=['get'],
        detail=False,
        url_path='fetch'
    )
    def list_analysis(self, request, *args, **kwargs):
        response = ["check 1"]
        return Response(response, status=http_status.HTTP_200_OK)
