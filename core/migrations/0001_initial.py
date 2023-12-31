# Generated by Django 4.2.4 on 2023-09-13 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ocorrencias',
            fields=[
                ('inserido', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Inserido em:')),
                ('atualizado', models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em:')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('id_ocorrencia', models.AutoField(primary_key=True, serialize=False)),
                ('id_user', models.CharField(max_length=45, verbose_name='user_id')),
                ('user', models.CharField(max_length=45, verbose_name='Usuário')),
                ('data_registro', models.DateField(help_text='Data em que foi visualizada a praga.', verbose_name='Data da Ocorrência')),
                ('praga', models.CharField(help_text='Selecione qual o tipo de praga esta contaminando.', max_length=40)),
                ('Cultura', models.CharField(help_text='Qual plantação foi contaminada?', max_length=45)),
                ('status', models.CharField(choices=[('Controlada', 'Controlada'), ('Fora de Controle', 'Fora de Controle')], help_text='A praga esta controlada?', max_length=45, verbose_name='Controlada?')),
                ('nome_propriedade', models.CharField(help_text='Nome da propriedade que esta sendo contaminada.', max_length=60, verbose_name='Nome da Propriedade afetada')),
                ('prejuizo', models.DecimalField(decimal_places=2, default=0.0, help_text='qual o valor do prejuizo?', max_digits=20, verbose_name='Total do prejuizo R$')),
                ('hectares', models.IntegerField(default=0, help_text='quantos hectares estão contaminados', verbose_name='Quantidade de hectar afetado')),
                ('latitude', models.CharField(max_length=45)),
                ('longitude', models.CharField(max_length=45)),
                ('imagens', stdimage.models.StdImageField(blank=True, force_min_size=False, help_text='Selecione as imagens da praga.', null=True, upload_to='images', variations={}, verbose_name='Imagem')),
                ('Observações', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Tabela de Ocorrência',
                'verbose_name_plural': 'Tabela de Ocorrência',
            },
        ),
        migrations.CreateModel(
            name='Tb_Registros',
            fields=[
                ('inserido', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Inserido em:')),
                ('atualizado', models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em:')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('id_ocorrencia', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=45)),
                ('Data da Ocorrência', models.DateField(help_text='Data em que foi visualizada a praga.')),
                ('praga', models.CharField(help_text='Selecione qual o tipo de praga esta contaminando.', max_length=40)),
                ('cultura', models.CharField(blank=True, help_text='Qual plantação foi contaminada?', max_length=45, null=True, verbose_name='Cultura')),
                ('status', models.CharField(choices=[('Controlada', 'Controlada'), ('Fora de Controle', 'Fora de Controle')], help_text='A praga esta controlada?', max_length=45, verbose_name='A Praga Esta Controlada?')),
                ('nome_propriedade', models.CharField(blank=True, help_text='Nome da propriedade que esta sendo contaminada.', max_length=60, null=True, verbose_name='Nome da Propriedade:')),
                ('prejuizo', models.DecimalField(decimal_places=2, default=0.0, help_text='qual o valor do prejuizo?', max_digits=20, verbose_name='Total do prejuizo R$')),
                ('hectares', models.IntegerField(default=0, help_text='quantos hectares estão contaminados', verbose_name='Quantidade de hectar afetado')),
                ('latitude', models.CharField(max_length=45)),
                ('longitude', models.CharField(max_length=45)),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, help_text='Selecione as imagens da praga.', null=True, upload_to='images', variations={}, verbose_name='Imagem')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observações')),
            ],
            options={
                'verbose_name': 'Tabela de Registro',
                'verbose_name_plural': 'Tabela de Registros',
            },
        ),
        migrations.CreateModel(
            name='TbPragas',
            fields=[
                ('id_praga', models.AutoField(primary_key=True, serialize=False)),
                ('cultura', models.CharField(blank=True, max_length=45, null=True)),
                ('especie', models.CharField(blank=True, max_length=45, null=True)),
                ('nome_comum', models.CharField(max_length=45)),
                ('nome_comum2', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Tabela de Praga',
                'verbose_name_plural': 'Tabela de Pragas',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tabela de Perfil',
                'verbose_name_plural': 'Tabela de Perfis',
            },
        ),
    ]
