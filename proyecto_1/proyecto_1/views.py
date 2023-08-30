from django.http import HttpResponse
import datetime

def saludo(reques):

    return HttpResponse("Hola holas")

def nosvemos(reques):
    return HttpResponse("bai")

def fechaActual(request):
    fecha_actual = datetime.datetime.now()
    docum = "<h1>La hora es: %s</h1>" % fecha_actual
    return HttpResponse(docum)

def calcularEdad(reques, edadActual, anio):
    # edadActual = 189
    periodo = anio - 2023
    edadFutura = edadActual + periodo
    docum = "<h1>En el anio %s tendras %s años</h1>" % (anio, edadFutura)
    return HttpResponse(docum)
