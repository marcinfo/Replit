from django.contrib import admin
from .models import Profile, Tb_Registros, TbPragas,TbCadastro_culturas,TbCadastro_pragas,TbParametros


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


@admin.register(Tb_Registros)
class Tb_OcorrenciasAdmin(admin.ModelAdmin):
    list_display = ['id_ocorrencia','ativo','usuario','inserido','cultura', 'praga','status','imagem', 'nome_propriedade',
                    'hectares', 'prejuizo', 'latitude', 'longitude', 'observacao']
    search_fields = ('id_ocorrencia','inserido', 'praga')
    ordering = ['id_ocorrencia','inserido','praga']


@admin.register(TbPragas)
class TbPragasAdmin(admin.ModelAdmin):
    list_display = [ 'cultura','especie', 'nome_comum', 'nome_comum2']
@admin.register(TbCadastro_pragas)
class TbCadastro_pragasAdmin(admin.ModelAdmin):
    list_display = ['id', 'especie', 'nome_comum']
    ordering = ['nome_comum','id']

@admin.register(TbCadastro_culturas)
class TbCadastro_culturasAdmin(admin.ModelAdmin):
    list_display = [ 'id','cultura', 'nome_comum']
    ordering = ['cultura', 'nome_comum']

    @admin.register(TbParametros)
    class TbParametrosAdmin(admin.ModelAdmin):
        list_display = ['id', 'hora_envio']
        ordering = ['hora_envio','id' ]
