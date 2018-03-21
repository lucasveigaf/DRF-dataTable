from risk.models import Risk, Responses
from risk.serializers import RiskSerializer, ResponsesSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.template.response import TemplateResponse
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.exceptions import ObjectDoesNotExist

def country(request, path, instance, extra):
    if not instance:
        return render(request, "404.html")

    return render(
        request,
        'risk/country.html',
        {
            'instance': instance,
            'children': instance.get_children()
        }
    )


def risk(request, path, instance, extra):
    if not instance:
        return render(request, "404.html")

    return render(
        request,
        'risk/dashboard_1.html',
        {
            'instance': instance,
            'children': instance.get_children()
        }
    )

def dashboard_2(request):
    html = TemplateResponse(request, 'dashboard_2.html')
    return HttpResponse(html.render())

class RiskViewSet(viewsets.ModelViewSet):

    def list(self, request, **kwargs):
        result = dict()
        result['data'] = []
        result['recordsTotal'] = 0
        try:
            qs = Risk.objects.get(slug=kwargs['risk_slug']).get_descendants(include_self=True)            
            if not qs: # If Risk has no children, DoesNotExist will also be thrown
                raise Risk.DoesNotExist

            serializedResult = RiskSerializer(qs, many=True)
            result['data'] = serializedResult.data
            result['recordsTotal'] = qs.count()
            return Response(result, status=status.HTTP_200_OK)

        except Risk.DoesNotExist as e:
            # if you add an error attribute to the response, dataTables plugin will
            # automatically show an alert. And by default, will alert() if response
            # code is != 200
            # result['error'] = "No risk found"
            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            return Response("Something went very wrong")

class ResponsesViewSet(viewsets.ModelViewSet):

    def list(self, request, **kwargs):
        result = dict()
        result['data'] = []
        result['recordsTotal'] = 0
        try:
            risk = Risk.objects.get(slug=kwargs['response_slug']).get_descendants(include_self=True)
            qs = Responses.objects.filter(risk__in=risk)
            if not qs:
                raise Responses.DoesNotExist

            serializedResult = ResponsesSerializer(qs, many=True)
            result['data'] = serializedResult.data
            result['recordsTotal'] = qs.count()
            return Response(result, status=status.HTTP_200_OK)

        except Responses.DoesNotExist as e:
            # if you add an error attribute to the response, dataTables plugin will
            # automatically show an alert. And by default, will alert() if response
            # code is != 200
            # result['error'] = "No response found"
            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response("Something went very wrong")

