# Generated by Django 3.1.4 on 2020-12-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=400)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('completado', models.BooleanField(default=False)),
            ],
        ),
    ]
