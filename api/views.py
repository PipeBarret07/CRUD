from typing import Any
from django import http
from django.http.response import JsonResponse
from django.views import View
from .models import Company, Developer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {'message': 'Success', 'companies': company}
            else: 
                datos = {'message': 'companies not found...'}
        else:
            companies =  list(Company.objects.values())
            if len(companies) > 0:
                datos = {'message': 'Succes', 'companies': companies}
            else:
                datos = {'message': 'companies not found...'}

        return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Company.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        datos = { 'mesagge': 'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id = id).values())
        if (len(companies) > 0):
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            datos = {'message': 'Success'}
        else: 
                datos = {'message': 'companies not found...'}

        return JsonResponse(datos)


    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if (len(companies) > 0):
            Company.objects.filter(id=id).delete()
            datos = { 'mesagge': 'Success'}
        else: 
            datos = {'message': 'companies not found...'} 

        return JsonResponse(datos)       
    

class DeveloperView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id = 0):
        if(id > 0):
            developer = Developer.objects.get(id = id)
            if developer:
                datos = {'message': 'Success', 'Developer': developer}
            else: 
                datos = {'message': 'Developer not found...'}
        else:
            developers = list(Developer.objects.values())
            if(len(developers) > 0):
                datos = {'message': 'Success', 'Developers': developers}
            else: 
                datos = {'message': 'Developer not found...'}

        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        company = Company.objects.get(id=jd['company'])
        Developer.objects.create(name=jd['name'], company=company)
        datos = {'message': 'Success'}
        return JsonResponse(datos)    



