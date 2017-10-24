from django.shortcuts import render
from django.shortcuts import routers, serializers, viewsets
from eventosapp.models import *
from eventosapp.serializers import *

# Create your views here.
class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class PessoaViewSet (viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
class EventoViewSet (viewsets.ModelViewSet):
    queryset= Evento.objects.all()
    serializer_class = EventoSerializer
class TicketViewSet (viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
class InscricaoViewSet (viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
