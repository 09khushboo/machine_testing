from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Client

# Create your views here.
from rest_framework import viewsets
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


def home(request):
    return HttpResponse("<h1>Welcome to Project Management System</h1>")


def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        client.client_name = request.POST['client_name']
        client.save()
        return redirect('client_list')  
    return render(request, 'edit_client.html', {'client': client})

def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        client.delete()
        return redirect('client_list')  # Redirect after deleting
    return render(request, 'confirm_delete.html', {'client': client})
