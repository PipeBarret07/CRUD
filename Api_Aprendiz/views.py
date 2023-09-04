from typing import Any
from django import http
from django.http.response import JsonResponse
from django.views import View
from .models import Aprendices
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class AprendicesViews(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            aprendices = list(Aprendices.objects.filter(id=id).values())
            if len(aprendices) > 0:
                aprendiz = aprendices[0]
                datos = {'message': '!Está el Aprendiz¡', 'aprendices': aprendiz}
            else: 
                datos = {'message': 'El aprendiz no está...'}
        else:
            aprendices =  list(Aprendices.objects.values())
            if len(aprendices) > 0:
                datos = {'message': '!Está el Aprendiz¡', 'aprendices': aprendices}
            else:
                datos = {'message': 'El aprendiz no está registrado...'}

        return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Aprendices.objects.create(nombres=jd['nombres'], apellidos=jd['apellidos'], año=jd['año'], documento=jd['documento'], tipo_de_documento=jd['tipo_de_documento'], numero_de_ficha=jd['numero_de_ficha'])
        datos = { 'mesagge': 'Se ha registrado'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        aprendices = list(Aprendices.objects.filter(id = id).values())
        if (len(aprendices) > 0):
            aprendiz = Aprendices.objects.get(id=id)
            aprendiz.nombres = jd['nombres']
            aprendiz.apellidos = jd['apellidos']
            aprendiz.año = jd['año']
            aprendiz.documento = jd['documento']
            aprendiz.tipo_de_documento = jd['tipo_de_documento']
            aprendiz.numero_de_ficha= jd['numero_de_ficha']
            aprendiz.save()
            datos = {'message': 'Se ha modificado los datos'}
        else: 
                datos = {'message': 'El aprendiz no está registrado...'}

        return JsonResponse(datos)


    def delete(self, request, id):
        aprendices = list(Aprendices.objects.filter(id=id).values())
        if (len(aprendices) > 0):
            Aprendices.objects.filter(id=id).delete()
            datos = { 'mesagge': 'Se han eleminado los datos'}
        else: 
            datos = {'message': 'El aprendiz no está registrado...'} 

        return JsonResponse(datos)       
    
