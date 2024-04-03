# Generated by Django 5.0.3 on 2024-03-29 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_alter_custoaquisicao_ca_alter_custoaquisicao_icms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custoaquisicao',
            name='CA',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='custoaquisicao',
            name='ICMS',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='custoaquisicao',
            name='alimento',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='custoaquisicao',
            name='aluguel',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='custoaquisicao',
            name='frete',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='custoaquisicao',
            name='hospedagem',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='custoaquisicao',
            name='internet',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='custoaquisicao',
            name='luz',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='custoaquisicao',
            name='sacola',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='custoaquisicao',
            name='salario',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='custoaquisicao',
            name='taxa_cartao',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='custoaquisicao',
            name='trafego_pago',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='margemlucro',
            name='casual',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='margemlucro',
            name='fitness',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='margemlucro',
            name='intima',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='margemlucro',
            name='jeans',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='margemlucro',
            name='praia',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='produto',
            name='margem_lucro',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='produto',
            name='valor_aquisicao',
            field=models.FloatField(default=0.0),
        ),
    ]
