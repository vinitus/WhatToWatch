# Generated by Django 3.2.6 on 2022-11-23 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('overview', models.TextField()),
                ('poster_path', models.TextField(null=True)),
                ('popularity', models.FloatField()),
                ('release_date', models.TextField()),
                ('runtime', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('backdrop_path', models.TextField(null=True)),
                ('original_language', models.TextField()),
                ('adult', models.BooleanField()),
                ('country', models.CharField(max_length=30, null=True)),
                ('belongs_to_collection', models.IntegerField(null=True)),
                ('genres', models.ManyToManyField(to='api.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='NetflixTop10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('title', models.TextField()),
                ('release_date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WatchaTop10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('title', models.TextField()),
                ('release_date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo_path', models.TextField()),
                ('movies', models.ManyToManyField(to='api.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('movies', models.ManyToManyField(to='api.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('movies', models.ManyToManyField(to='api.Movie')),
            ],
        ),
    ]
