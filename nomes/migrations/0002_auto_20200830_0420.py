# Generated by Django 2.2.3 on 2020-08-30 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nome',
            name='detalhes',
            field=models.TextField(),
        ),
    ]
