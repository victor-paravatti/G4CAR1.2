from django.contrib import admin
from core.models import Cliente, Veiculo, Parametro, Movimento, Mensalista

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Parametro)
admin.site.register(Movimento)
admin.site.register(Mensalista)
