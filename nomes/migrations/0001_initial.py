# Generated by Django 2.2.3 on 2020-08-30 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nome',
            fields=[
                ('codigo_nome', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Código do Nome')),
                ('nome', models.CharField(max_length=50)),
                ('significado', models.CharField(max_length=50)),
                ('detalhes', models.TextField(max_length=50)),
                ('slug', models.SlugField()),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
