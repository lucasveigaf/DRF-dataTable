from risk.models import Risk, Responses
from risk.models import query_risk_by_args, query_responses_by_args
from risk.serializers import RiskSerializer, ResponsesSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response

from django.template.response import TemplateResponse
from django.http.response import HttpResponse

from django.shortcuts import get_object_or_404, render, redirect


#Breadcrumbs - Risk (Used by django-mptt-urls) ----------------------------------------------------

def risk(request, path, instance, extra):
    return render(
        request,
        'risk/risk.html',

        {
            'instance': instance,
            'children': instance.get_children() if instance else Risk.objects.root_nodes(),
            'extra': extra,
        }
    )

"""
# Risk page--------------------------

def risks(request):
    html = TemplateResponse(request, 'risks.html')
    return HttpResponse(html.render())


# Dashboard page--------------------------

def dashboard(request):
    html = TemplateDashboard(request, 'dashboard.html')
    return HttpResponse(html.render())
"""


# Risk view sets for API and Datatable----------------------------

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



# Responses view sets for API and Datatable----------------------------

class ResponsesViewSet(viewsets.ModelViewSet):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer

    def list(self, request, **kwargs):
        try:
            responses = query_responses_by_args(**request.query_params)
            serializer = ResponsesSerializer(responses['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = responses['draw']
            result['recordsTotal'] = responses['total']
            result['recordsFiltered'] = responses['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)

