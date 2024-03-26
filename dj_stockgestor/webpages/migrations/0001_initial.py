# Generated by Django 5.0.1 on 2024-03-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=40)),
                ('cnpj', models.CharField(max_length=18)),
                ('inscricao_estadual', models.CharField(max_length=15)),
                ('inscricao_municipal', models.CharField(max_length=15)),
                ('fornecedor_email', models.EmailField(max_length=40)),
                ('fornecedor_telefone', models.CharField(max_length=12)),
            ],
        ),
    ]
