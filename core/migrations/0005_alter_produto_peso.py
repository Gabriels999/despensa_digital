# Generated by Django 4.1.1 on 2022-09-11 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_produto_em_estoque_produto_necessario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='peso',
            field=models.FloatField(),
        ),
    ]
