# Generated by Django 5.0.3 on 2024-03-30 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_alter_venda_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='custoaquisicao',
            name='total_adquirido',
            field=models.FloatField(default=0),
        ),
    ]
