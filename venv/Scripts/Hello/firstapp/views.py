from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def index(request):
    header = 'Personal data'
    langs = ['English', 'German', 'Spanish']
    user = {'name': 'Tom', 'age': 23}
    address = ('Apple', 23, 45)
    data = {'header': header, 'langs': langs, 'user': user, 'address': address}
    return render(request, 'firstapp/home.html', context=data)

def about(request):
    output = '<h2>About</h2>'
    return HttpResponse(output)

def contacts(request):
    output = '<h2>Contacts</h2>'
    return HttpResponse(output)

def products(request):
    productid = request.GET.get("pid", 0)
    category = request.GET.get("cat", "None")
    output = '<h2>Product № {0}  Category: {1}</h2>'.format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get('id', 1)
    name = request.GET.get('name', 'Tom')
    output = '<h2>User</h2><h3>id: {0}  name: {1}</h3>'.format(id, name)
    return HttpResponse(output)