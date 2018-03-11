from risk.models import Risk, Hazard
from risk.models import query_risk_by_args, query_hazard_by_args
from risk.serializers import RiskSerializer, HazardSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response

from django.template.response import TemplateResponse
from django.http.response import HttpResponse


def hazards(request):
    html = TemplateResponse(request, 'hazard.html')
    return HttpResponse(html.render())


class HazardViewSet(viewsets.ModelViewSet):
    queryset = Hazard.objects.all()
    serializer_class = HazardSerializer

    def list(self, request, **kwargs):
        try:
            hazard = query_hazard_by_args(**request.query_params)
            serializer = HazardSerializer(hazard['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = hazard['draw']
            result['recordsTotal'] = hazard['total']
            result['recordsFiltered'] = hazard['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)











def risks(request):
    html = TemplateResponse(request, 'index2.html')
    return HttpResponse(html.render())


class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

    def list(self, request, **kwargs):
        try:
            risk = query_risk_by_args(**request.query_params)
            serializer = RiskSerializer(risk['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = risk['draw']
            result['recordsTotal'] = risk['total']
            result['recordsFiltered'] = risk['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)

            # [Get] api/risk/
            # def list(self, request, **kwargs):
            #     try:
            #         risk = Risk.objects.all()[0:50000]
            #         serializer = RiskSerializer(risk, many=True)
            #
            #         return Response(serializer.data, status=status.HTTP_200_OK, template_name=None, content_type=None)
            #
            #     except Exception as e:
            #         return Response(e.message, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)
            #
