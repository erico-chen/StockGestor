# Generated by Django 5.0.1 on 2024-03-26 22:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webpages", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="fornecedores",
            name="endereco",
            field=models.CharField(default="NULL", max_length=40),
        ),
        migrations.AddField(
            model_name="fornecedores",
            name="uf",
            field=models.CharField(default="NULL", max_length=2),
        ),
    ]
