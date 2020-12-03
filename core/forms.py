from core.models import Cliente, Veiculo
from django.forms import ModelForm


class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class FormVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
