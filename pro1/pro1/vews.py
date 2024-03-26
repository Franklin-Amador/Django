from django.http import HttpResponse
from django.template import Template, Context

class Auto(object):
    def __init__(self, nombre, marca):
        self.nombre=nombre
        self.marca=marca

def saludo(request):
    
    a1 = Auto("Camaro", "Chevrolet")
    doc_externo=open("C:/Users/joela/Desktop/Pasatiempos/Django/pro1/pro1/plantillas/pnt1.html")
    
    #name="Fran"
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_auto": a1.nombre, "marca_auto":a1.marca })
    
    doc = plt.render(ctx)
    return HttpResponse(doc)