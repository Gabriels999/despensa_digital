# Generated by Django 4.1.1 on 2022-09-10 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.CharField(default='Cozinha', max_length=64),
        ),
    ]
