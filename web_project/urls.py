from django.contrib import admin
from django.urls import path, include
from core.views import home, cadastro_cliente, listagem_clientes, \
    cadastro_veiculo, listagem_veiculos, Registrar, atualiza_cliente, \
    exclui_cliente, cadastro_parametro, listagem_parametros, \
    atualiza_parametro, cadastro_mensalista, listagem_mensalistas, \
    exclui_parametro
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('registrar/', Registrar.as_view(), name='url_Registrar'),
    path('', home, name='url_principal'),
    path('cadastro_cliente/', cadastro_cliente, name='url_cadastro_cliente'),
    path('listagem_clientes/', listagem_clientes, name='url_listagem_clientes'),
    path('listagem_veiculos/', listagem_veiculos, name='url_listagem_veiculos'),
    path('cadastro_veiculo/', cadastro_veiculo, name='url_cadastro_veiculo'),
    path('atualiza_cliente/<int:id>/', atualiza_cliente, name='url_atualiza_cliente'),
    path('exclui_cliente/<int:id>/', exclui_cliente, name="url_exclui_cliente"),
    path('cadastro_parametro/', cadastro_parametro, name='url_cadastro_parametro'),
    path('listagem_parametros/', listagem_parametros, name='url_listagem_parametros'),
    path('atualiza_parametro/<int:id>', atualiza_parametro, name='url_atualiza_parametro'),
    path('exclui_parametro/<int:id>/', exclui_parametro, name='url_exclui_parametro'),
    path('cadastro_mensalista/', cadastro_mensalista, name='url_cadastro_mensalista'),
    path('listagem_mensalistas/', listagem_mensalistas, name='url_listagem_mensalistas'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
