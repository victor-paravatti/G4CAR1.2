from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_cliente', blank=True, null=True)

    def __str__(self):
        return self.nome + '(' + str(self.id) + ')'

    class Meta:
        verbose_name_plural = 'Clientes'


class Veiculo(models.Model):
    fabricante = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.CharField(max_length=4, blank=True, null=True)
    cor = models.CharField(max_length=20, blank=True, null=True)
    placa = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='fotos_cliente', blank=True, null=True)
    id_cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)

    def __str__(self):
        return self.placa

    class Meta:
        verbose_name_plural = 'Veiculos'
