# Generated by Django 4.1.2 on 2022-10-20 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coorientador', '0001_initial'),
        ('autor', '0001_initial'),
        ('orientador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data', models.DateField()),
                ('resumo', models.TextField(max_length=400)),
                ('palavras_chave', models.CharField(max_length=200)),
                ('universidade', models.CharField(max_length=200)),
                ('curso', models.CharField(max_length=200)),
                ('pdf', models.URLField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autor.autor')),
                ('coorientador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coorientador.coorientador')),
                ('orientador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orientador.orientador')),
            ],
        ),
    ]
