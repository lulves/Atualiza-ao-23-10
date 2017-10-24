from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from eventosapp.models import *

class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','is_staff')

class PessoaSerializer (serializers.HyperlinkedModelSerializer):
    usuarios = UserSerializer(many=False)

    class Meta:
        model = Pessoa
        fields = ('nome', 'usuarios')

class EventoSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('nome', )

class TicketSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('descricao','valor')

class InscricaoSerializer (serializers.HyperlinkedModelSerializer):
    evento = EventoSerializer (many=False)
    pessoa = PessoaSerializer (many=False)
    ticket = TicketSerializer (many=False)
    class Meta:
        model = Inscricao
        fields = ('evento')
