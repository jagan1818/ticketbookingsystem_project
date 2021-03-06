# Generated by Django 3.0.5 on 2022-02-15 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'shows_cities',
            },
        ),
        migrations.CreateModel(
            name='Theatres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('theatre_name', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.Cities')),
            ],
            options={
                'db_table': 'shows_theatres',
            },
        ),
        migrations.CreateModel(
            name='Screens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('screen_name', models.CharField(max_length=255)),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.Theatres')),
            ],
            options={
                'db_table': 'shows_screens',
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie_name', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.Screens')),
            ],
            options={
                'db_table': 'shows_movies',
            },
        ),
    ]
