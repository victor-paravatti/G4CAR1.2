from core.models import Cliente, Veiculo, Parametro, Movimento, Mensalista
from django.forms import ModelForm


class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class FormVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class FormParametro(ModelForm):
    class Meta:
        model = Parametro
        fields = '__all__'


class FormMovimento(ModelForm):
    class Meta:
        model = Movimento
        fields = '__all__'


class FormMensalista(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'

