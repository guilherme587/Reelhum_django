# Generated by Django 5.0.3 on 2024-03-30 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_custoaquisicao_total_adquirido_revenda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='margem_lucro',
            field=models.FloatField(default=0.7),
        ),
    ]