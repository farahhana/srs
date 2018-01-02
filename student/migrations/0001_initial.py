# Generated by Django 2.0.1 on 2018-01-02 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icnum', models.CharField(max_length=12, unique=True, verbose_name='IC Number')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('Course', models.CharField(choices=[('PR', 'Programming'), ('NT', 'Networking'), ('PC', 'PC Technichian')], default='PC', max_length=2, verbose_name='coursework')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created DateTimeField')),
                ('creatby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
