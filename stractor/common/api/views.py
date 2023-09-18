
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status as http_status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.db.models import Q, F


from stractor.common.models import Distributor
from stractor.common.serializers.serializers import DistributorSerializer


class DistributorViewSet(ListModelMixin, GenericViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer

    @swagger_auto_schema(
        tags=["distributor"],
        operation_id="distributor list",
        responses={200: DistributorSerializer(many=True)})
    @action(
        methods=['get'],
        detail=False,
        url_path='fetch'
    )
    def list_analysis(self, request, *args, **kwargs):
        entity_filter = request.query_params.get('entity',None) 
        # results = Distributor.objects.filter(Q(name__icontains=entity_filter) | Q(vid=entity_filter)) #filter for searching the people with their id or names

        queryset = Distributor.objects.prefetch_related('upline').values(
            'id', 
            'registration_date',
            'designation', 
            'name', 
            'percentage',
            'prev_cumpv',
            'exclusive_pv',
            'self_pv',
            'group_pv',
            'total_pv' , 
            'short_points', 
            'next_level_percentage',
            'vid',
            'upline_id', 
            'address',
            'phone_number',
            upline_name=F('upline__name')
        )

        # print("dadsss",results)

        response = DistributorSerializer(queryset, many=True)

        return Response(response.data, status=http_status.HTTP_200_OK)
    

