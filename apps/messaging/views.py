from django.shortcuts import get_object_or_404, render

from apps.properties.models import Property


def index(request):
    return render(request, 'messaging/index.html')


def properties(request):
    return render(request, 'messaging/properties.html')


def room(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    room_name = f"property_{property_id}"
    return render(request, 'messaging/messages.html', {
        'room_name': room_name, 
        'property_id': property_id,
        'property_title': property.title,
        })


# def view_messages(request):
#     return render(request, 'messaging/messages/<int:property_id>/.html') 
  
  
  
  
  
    
# def view_products(request):
#     return render(request, 'core/products.html', {
#         'categories': todos_los_productos
#     }
#                   )    
    # def contacto(request):
#     return render(request, 'core/contacto.html')

# class About(View):
#     def get(self, request):
#     


# from django.views import View
# from apps.messaging.models import MessageModel

#from .forms import

# Create your views here.

# def inicio(request):
#     nombre = "Fabrizio"
#     comidas_favoritas = ['lasagna', 'pizza', 'milanesas']
#     datos = {
#         'nombre': nombre,
#         'comidas': comidas_favoritas
#     }
#     return render(request, 'messaging/index.html', datos)

