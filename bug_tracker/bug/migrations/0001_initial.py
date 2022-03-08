# Generated by Django 4.0.3 on 2022-03-08 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
            ],
        ),
    ]
