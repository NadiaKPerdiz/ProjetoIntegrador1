# Generated by Django 3.2.8 on 2021-11-13 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matriculaApp', '0002_auto_20211113_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_presenca', models.DateField()),
                ('presente', models.BooleanField()),
                ('crianca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculaApp.matricula')),
            ],
        ),
    ]
