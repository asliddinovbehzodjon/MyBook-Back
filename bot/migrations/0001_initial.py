# Generated by Django 4.1.4 on 2023-01-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('t_id', models.CharField(max_length=20, unique=True)),
                ('language', models.CharField(default='en', max_length=5)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
