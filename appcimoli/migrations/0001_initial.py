# Generated by Django 4.0.4 on 2022-05-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deporte', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
    ]
